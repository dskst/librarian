# Librarian

Librarian is Book management system.  
Book registration and  rental management can be done.

## Description

Has the following functions.

1. Register for rental book.
2. Lend for book.
3. Return for lent book.

The lender's manager will use the NFC reader.  
Link NFC IDm with the entered user ID and skip enter user ID for the next time.  
ISBN code is used for the key of the book, and linked to user ID.

## Dependency

- Python 2.7
- nfcpy https://github.com/nfcpy/nfcpy
- luigi https://github.com/spotify/luigi
- Google Book APIs https://developers.google.com/books/
- (Google Cloud Datastore)  
TODO Eliminate dependency

## Setup

### for Docker

```
$ docker build --tag dskst/librarian .
```

Add that device to the container with `--device=` option.  
(See https://hub.docker.com/r/warapy/nfcpy-tagtool/ )

```
$ docker run --device=/dev/bus/usb/001/001 -it dskst/librarian
```

### for Mac

Please execute Python file as it is.

### Use Google Cloud Datastore

Read the authentication file.
```
$ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

Make entity for Google Cloud Datastore.

for example
```
Kind: Book
Key: Book name:9784873117768
Key literal: Key(Book, '9784873117768')

createdAt: 2018-07-10 (08:35:35.113) JST Indexed
description: Dockerを活用するために求められる知識・技術を総合的に解説。セキュリティやモニタリングと行った運用面まで踏み込んだ内容。
imageLinks: {"thumbnail":"http://books.google.com/books/content?id=BFsovgAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api","smallThumbnail":"http://books.google.com/books/content?id=BFsovgAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api"}
isLent: false
latestLender: abi01082 Indexed
renders: [{"userId":"test123","isLent":true,"createdAt":"2018-08-04T10:43:30.913143Z"},{"userId":"test456","isLent":false,"createdAt":"2018-08-04T10:45:15.343265Z"}] Indexed
stockedAt: 2018-07-10 (08:35:35.113) JST Indexed
title: Docker Indexed
updatedAt: 2018-08-04 (19:45:15.343) JST Indexed
```

## Usage

1. Register for rental book
```
python tasks/library_books.py BookRegister --local-scheduler
Please enter the ISBN code starting with 9 :
9784873113890
ISBN:9784873113890 is registered
```

2. Lent for book  
```
$ python tasks/library_books.py Rental --local-scheduler
Please NFC card　on the reader:
Reading...
Please enter the ID:
test123
Please enter the ISBN code starting with 9 :
9784873117768
[入門Python3] Rental is completed!
```

3. Return for lent book  
```
$ python tasks/library_books.py Rental --local-scheduler
Please NFC card　on the reader:
Reading...
Please enter the ISBN code starting with 9 :
9784873117386
[入門Python3] Returning is completed!
```

## Tests

```
$ python -m unittest discover -s ./tests
```
