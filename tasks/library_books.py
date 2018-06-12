# coding:utf-8
import datetime
import json
import re
import luigi # luigi (2.7.5)
import requests # pip requests (2.18.4)
import nfc # pip nfcpy (0.13.4)
from google.cloud import datastore # pip google-cloud-datastore

class Lender(luigi.Task):

    user_key = luigi.Parameter(default='')
    id_name = luigi.Parameter()

    def run(self):
        user_id = ''
        while not user_id:
            user_id = raw_input('Please enter the {id_name}:\n'.format(id_name=self.id_name))
            if user_id:
                # TODO: regex
                break

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

    isbn = luigi.Parameter(default='')
    search_api = luigi.Parameter()

    def run(self):
        while not self.isbn:
            self.isbn = raw_input('Please enter the ISBN code starting with 9 :\n')
            if self.isbn:
                # TODO: regex
                break

        try:
            r = requests.get(self.search_api + self.isbn)
        except Exception:
            raise RuntimeError('Could not connect to book search API')

        if r.status_code != requests.codes.ok:
            raise RuntimeError('Book not found')

        book_detail = r.json()

        if not book_detail['totalItems'] or int(book_detail['totalItems']) == 0:
            raise RuntimeError('Book not found')

        with self.output().open('w') as file:
            json.dump(book_detail, file)

    def output(self):
        return luigi.LocalTarget('data/books/{isbn}.json'.format(isbn=self.isbn))


class Rental(luigi.Task):

    isbn = luigi.Parameter(default='')
    user_key = luigi.Parameter(default='')

    def requires(self):
        return [BookSearch(self.isbn), Lender(self.user_key)]

    def run(self):
        print('{action} of books is completed!'.format(action='dummy'))

    def output(self):
        return luigi.LocalTarget(datetime.datetime.now().strftime('logs/%Y-%m-%d.%H%M%S.log'))

if __name__ == '__main__':
    luigi.run()