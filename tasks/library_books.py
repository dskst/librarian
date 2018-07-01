# coding:utf-8
import datetime
import json
import luigi # luigi (2.7.5)
import requests # pip requests (2.18.4)
import nfc # pip nfcpy (0.13.4)
import re
from google.cloud import datastore

class Lender(luigi.Task):

    user_key = luigi.Parameter(default='')
    id_name = luigi.Parameter()

    def run(self):
        user_id = self.input_user_id()

        with self.output().open('w') as file:
            file.write(user_id)

    def output(self):
        if not self.user_key:
            try:
                with nfc.ContactlessFrontend('usb') as clf:
                    clf.connect(rdwr={'on-connect': self.__nfc_connected, 'on-startup': self.__nfc_startup})
            except Exception:
                raise RuntimeError('NFC loading failed')

        return luigi.LocalTarget('data/users/{file}.dat'.format(file=self.user_key))

    def input_user_id(self):
        """
        Input for user id
            format is alphanumeric and some symbols.
        :return: input user id
        """
        user_id = ''
        while not user_id:
            user_id = raw_input('Please enter the {id_name}:\n'.format(id_name=self.id_name))
            if re.match(r"^[0-9a-zA-Z\.\-\_@]+$", user_id) is None:
                break

        return user_id

    def __nfc_startup(self, target):
        print 'Please NFC card　on the reader:'
        return target

    def __nfc_connected(self, tag):
        """
        Read IDM from NFC and setattr it
            format by tt3_sony https://github.com/nfcpy/nfcpy/blob/master/src/nfc/tag/tt3_sony.py
        :param tag:
        :return True:
        """
        tag_details = re.search('(.*)\sID=(.*)\sPMM=(.*)\sSYS=(.*)', str(tag))
        self.user_key = tag_details.group(2)
        print 'Reading...'
        return True


class BookSearch(luigi.Task):
    """
    Book search from ISBN code
    """

    isbn = luigi.Parameter(default='')
    search_api = luigi.Parameter()

    def run(self):
        self.isbn = self.input_isbn(self.isbn)
        response = self.search(self.isbn)

        with self.output().open('w') as file:
            json.dump(response, file)

    def output(self):
        return luigi.LocalTarget('data/books/{isbn}.json'.format(isbn=self.isbn))

    def input_isbn(self, isbn):
        """
        Input for ISBN code
        :param isbn:
        :return: isbn code
        """
        while re.match(r"^[0-9]{13}$", isbn) is None:
            isbn = raw_input('Please enter the ISBN code starting with 9 :\n')

        return isbn

    def search(self, isbn):
        """
        Search from Google Books API
        :param isbn: 13 digit ISBN code
        :return: book detail for json
        """
        if not isbn:
            raise RuntimeError('ISBN must not empty')

        try:
            r = requests.get(self.search_api + isbn)
        except Exception:
            raise RuntimeError('Could not connect to book search API')

        if r.status_code != requests.codes.ok:
            raise RuntimeError('Status code is ' + r.status_code)

        book_detail = r.json()

        if not book_detail['totalItems'] or int(book_detail['totalItems']) == 0:
            raise RuntimeError('Book is not found')

        return book_detail


class Rental(luigi.Task):

    isbn = luigi.Parameter(default='')
    user_key = luigi.Parameter(default='')

    def requires(self):
        return {'book':BookSearch(self.isbn), 'user':Lender(self.user_key)}

    def run(self):
        with self.input()['book'].open('r') as file:
            book = json.loads(file.read())
            if not self.isbn:
                for identifier in book['items'][0]['volumeInfo']['industryIdentifiers']:
                    if identifier['type'] == 'ISBN_13':
                        self.isbn = identifier['identifier']

        with self.input()['user'].open('r') as file:
            userid = file.read()

        # Fetch data of book and lender
        client = datastore.Client()
        key = client.key('Book', self.isbn)
        response = client.get(key)

        if response is None:
            message = '[WARNING]Book not registered. ISBN:{isbn}'.format(isbn=self.isbn)

        else:
            data = datastore.Entity(key = key, exclude_from_indexes = ['description', 'imageLinks', 'isLent'])

            now = datetime.datetime.now()
            is_lent = True if response['isLent'] == False else False

            renders = []
            if 'renders' in response:
                renders.extend(response['renders'])
            renders.extend([{'userId':unicode(userid), 'isLent':is_lent, 'createdAt': now}])

            data['title'] = book['items'][0]['volumeInfo']['title']
            data['description'] = book['items'][0]['volumeInfo']['description']
            data['imageLinks'] = book['items'][0]['volumeInfo']['imageLinks']
            data['latestLender'] = unicode(userid)
            data['isLent'] = is_lent
            data['renders'] = renders
            data['createdAt'] = response['createdAt']
            data['updatedAt'] = now

            with client.transaction():
                client.put(data)

            action = 'Rental' if is_lent == True else 'Returning'
            message = '[{title}] {action} is completed!'.format(title=data['title'].encode('utf_8'), action=action)
            print message

        with self.output().open('w') as file:
            file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S {message}'.format(message=message)))

    def output(self):
        return luigi.LocalTarget(datetime.datetime.now().strftime('logs/%Y-%m-%d.%H%M%S.rental.log'))


class BookRegister(luigi.Task):

    isbn = luigi.Parameter(default='')

    def requires(self):
        return BookSearch(self.isbn)

    def run(self):
        """
        Search book from Google Cloud Datastore.
        If book does not exist, it is newly registered.
        TODO: Make it work on other then Google Cloud Datastore.
        """

        # Search for Google Cloud Datastore
        client = datastore.Client()
        key = client.key('Book', self.isbn)
        response = client.get(key)

        if response is not None:
            result = 'already exist'

        else:
            data = datastore.Entity(key = key, exclude_from_indexes = ['description', 'imageLinks', 'isLent'])
            now = datetime.datetime.now()

            with self.input().open('r') as file:
                book = json.loads(file.read())

            data['title'] = book['items'][0]['volumeInfo']['title']
            data['description'] = book['items'][0]['volumeInfo']['description']
            data['imageLinks'] = book['items'][0]['volumeInfo']['imageLinks']
            data['isLent'] = False
            data['createdAt'] = now
            data['updatedAt'] = now

            client.put(data)
            result = 'registered'

        message = 'ISBN:{isbn} is {result}'.format(isbn=self.isbn, result=result)

        print message

        with self.output().open('w') as file:
            file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S {message}'.format(message=message)))

    def output(self):
        return luigi.LocalTarget(datetime.datetime.now().strftime('logs/%Y-%m-%d.register.{isbn}.log'.format(isbn=self.isbn)))

if __name__ == '__main__':
    luigi.run()