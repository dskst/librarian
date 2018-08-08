# Librarian

Librarian is Book management system.  
Book registration and  rental management can be done.

## Description

Has the following functions.

- Register for rental book.
- Lend for book.
- Return for lent book.

The lender's manager will use the NFC reader.  
Link NFC IDm with the entered user ID and skip enter user ID for the next time.  
ISBN code is used for the key of the book, and linked to user ID.

## Dependency

- Python 2.7
- nfcpy https://github.com/nfcpy/nfcpy
- luigi https://github.com/spotify/luigi
- Google Book APIs https://developers.google.com/books/

## Setup

### for Docker

```
$ docker build --tag dskst/librarian .
```

Add that device to the container with `--device=` option.  
https://hub.docker.com/r/warapy/nfcpy-tagtool/

```
$ docker run --device=/dev/bus/usb/001/001 -it dskst/librarian
```

### for Mac

Please execute Python file as it is.

## Usage

0. Register for rental book
```
```
1. Lent for book  
```
$ python tasks/library_books.py Rental --local-scheduler
Please NFC card　on the reader:
Reading...
Please enter the ID:
test123
Please enter the ISBN code starting with 9 :
9784873117768
```
2. Return for lent book  
