# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import datetime
import unittest
from tasks.builder import DataStoreBuilder


class DataStoreBuilderTest(unittest.TestCase):

    def setUp(self):
        self.entity = {}
        self.now = datetime.datetime.now()
        self.title = 'This is just Test'
        self.description = 'This is just Test. It\'s so cool'
        self.image_links = {"smallThumbnail": "http://books.google.com/books/content?id=YVTijgEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api", "thumbnail": "http://books.google.com/books/content?id=YVTijgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"}
        self.is_lent = True
        self.latest_lender = 'abc123'
        self.renders = [{'userId':'abc123', 'isLent':True, 'createdAt':self.now}, {'userId':'efc456', 'isLent':False, 'createdAt': self.now}]
        self.stocked_at = self.now
        self.created_at = self.now
        self.updated_at = self.now

    def test_add_tile_when_convert_unicode(self):
        builder = DataStoreBuilder(self.entity)
        builder.add_title(self.title)
        response = builder.get()
        self.assertEqual(unicode(self.title), response['title'])

    def test_add_description_when_convert_unicode(self):
        builder = DataStoreBuilder(self.entity)
        builder.add_description(self.description)
        response = builder.get()
        self.assertEqual(unicode(self.description), response['description'])
