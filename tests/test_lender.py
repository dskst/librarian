# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import luigi
import luigi.notifications
from helpers import LuigiTestCase

import __builtin__
from tasks.library_books import Lender

luigi.notifications.DEBUG = True

class LenderTest(LuigiTestCase):

    def test_input_user_id_when_input_is_alphanumeric(self):
        original = __builtin__.raw_input
        __builtin__.raw_input = lambda _: 'ABC123abc'
        self.assertEqual('ABC123abc', Lender(luigi.task).input_user_id())
        __builtin__.raw_input = original

    def test_input_user_id_when_input_is_symbol(self):
        original = __builtin__.raw_input
        __builtin__.raw_input = lambda _: '.-_@'
        self.assertEqual('.-_@', Lender(luigi.task).input_user_id())
        __builtin__.raw_input = original