# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import luigi
import luigi.notifications
from helpers import LuigiTestCase

import __builtin__
from tasks.library_books import BookSearch

luigi.notifications.DEBUG = True

class BookSearchTest(LuigiTestCase):

    # def test_run(self):
    #     __builtin__.raw_input = lambda _: '9784873117386'
    #     self.run_locally(['BookSearch'])
    #     # TODO: run's test

    def test_input_isbn_when_arg_and_res_same(self):
        isbn = '9784873117386'
        self.assertEqual('9784873117386', BookSearch(luigi.task).input_isbn(isbn))

    def test_input_isbn_when_input_value_is_returned(self):
        isbn = ''
        original = __builtin__.raw_input
        __builtin__.raw_input = lambda _: '0123456789012'
        self.assertEqual('0123456789012', BookSearch(luigi.task).input_isbn(isbn))
        __builtin__.raw_input = original

    def test_search_when_isbn_is_empty(self):
        with self.assertRaises(RuntimeError) as cm:
            BookSearch(luigi.task).search('')
        self.assertEquals(cm.exception.message, 'ISBN must not empty')

    def test_search_when_isbn_different_models(self):
        with self.assertRaises(RuntimeError) as cm:
            BookSearch(luigi.task).search('1')
        self.assertEquals(cm.exception.message, 'Book is not found')

    def test_search_when_isbn_not_exists(self):
        with self.assertRaises(RuntimeError) as cm:
            BookSearch(luigi.task).search('9999999999999')
        self.assertEquals(cm.exception.message, 'Book is not found')

    def test_search_when_normal(self):
        response = BookSearch(luigi.task).search('9784873117386')
        self.assertEquals(1, response['totalItems'])

