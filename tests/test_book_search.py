# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import luigi
import luigi.notifications
from luigi.mock import MockTarget
from helpers import LuigiTestCase

import __builtin__
from tasks.library_books import BookSearch

luigi.notifications.DEBUG = True

class BookSearchTest(LuigiTestCase):

    # def test_run(self):
    #     __builtin__.raw_input = lambda _: '9784873117386'
    #     self.run_locally(['BookSearch'])
    #     # TODO: run's tet

    def test_input_isbn_when_arg_and_res_same(self):
        isbn = '9784873117386'
        self.assertEqual('9784873117386', BookSearch(luigi.task).input_isbn(isbn))

    def test_input_isbn_when_input_value_is_returned(self):
        isbn = ''
        __builtin__.raw_input = lambda _: '0123456789012'
        self.assertEqual('0123456789012', BookSearch(luigi.task).input_isbn(isbn))