# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import unittest
import datetime
from tasks.director import RentalDirector, RegisterDirector
from tasks.builder import DataStoreBuilder

class DirectorTest(unittest.TestCase):

    def setUp(self):
        self.entity = {}
        self.now = datetime.datetime.now()

        # Make books
        self.book = {"totalItems": 1, "items": [{"kind": "books#volume", "volumeInfo": {"description": "Python\u304c\u8a95\u751f\u3057\u3066\u56db\u534a\u4e16\u7d00\u3002\u30c7\u30fc\u30bf\u30b5\u30a4\u30a8\u30f3\u30b9\u3084\u30a6\u30a7\u30d6\u958b\u767a\u3001\u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u306a\u3069\u3055\u307e\u3056\u307e\u306a\u5206\u91ce\u3067Python\u306e\u4eba\u6c17\u304c\u6025\u4e0a\u6607\u4e2d\u3067\u3059\u3002\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0\u6559\u80b2\u306e\u73fe\u5834\u3067\u3082C\u306b\u4ee3\u308f\u3063\u3066Python\u306e\u63a1\u7528\u304c\u5897\u3048\u3066\u304d\u3066\u3044\u307e\u3059\u3002\u672c\u66f8\u306f\u3001\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0\u304c\u521d\u3081\u3066\u3068\u3044\u3046\u4eba\u3092\u5bfe\u8c61\u306b\u66f8\u304b\u308c\u305f\u3001Python\u306e\u5165\u9580\u66f8\u3067\u3059\u3002\u524d\u63d0\u3068\u3059\u308b\u77e5\u8b58\u306f\u7279\u306b\u3042\u308a\u307e\u305b\u3093\u3002\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0\u304a\u3088\u3073Python\u306e\u57fa\u790e\u304b\u3089\u30a6\u30a7\u30d6\u3001\u30c7\u30fc\u30bf\u30d9\u30fc\u30b9\u3001\u30cd\u30c3\u30c8\u30ef\u30fc\u30af\u3001\u4e26\u884c\u51e6\u7406\u3068\u3044\u3063\u305f\u5fdc\u7528\u307e\u3067\u3001Python\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0\u3092\u308f\u304b\u308a\u3084\u3059\u304f\u4e01\u5be7\u306b\u8aac\u660e\u3057\u307e\u3059\u3002", "language": "ja", "publishedDate": "2015-12-01", "readingModes": {"text": False, "image": False}, "previewLink": "http://books.google.co.jp/books?id=YVTijgEACAAJ&dq=isbn:9784873117386&hl=&cd=1&source=gbs_api", "title": "\u5165\u9580Python3", "printType": "BOOK", "pageCount": 567, "maturityRating": "NOT_MATURE", "contentVersion": "preview-1.0.0", "industryIdentifiers": [{"identifier": "4873117380", "type": "ISBN_10"}, {"identifier": "9784873117386", "type": "ISBN_13"}], "imageLinks": {"smallThumbnail": "http://books.google.com/books/content?id=YVTijgEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api", "thumbnail": "http://books.google.com/books/content?id=YVTijgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"}, "authors": ["\u30d3\u30eb\u30eb\u30d0\u30ce\u30d3\u30c3\u30af"], "allowAnonLogging": False, "infoLink": "http://books.google.co.jp/books?id=YVTijgEACAAJ&dq=isbn:9784873117386&hl=&source=gbs_api", "canonicalVolumeLink": "https://books.google.com/books/about/%E5%85%A5%E9%96%80Python3.html?hl=&id=YVTijgEACAAJ"}, "searchInfo": {"textSnippet": "Python\u304c\u8a95\u751f\u3057\u3066\u56db\u534a\u4e16\u7d00\u3002\u30c7\u30fc\u30bf\u30b5\u30a4\u30a8\u30f3\u30b9\u3084\u30a6\u30a7\u30d6\u958b\u767a\u3001\u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u306a\u3069\u3055\u307e\u3056\u307e\u306a\u5206\u91ce\u3067Python\u306e\u4eba\u6c17\u304c\u6025\u4e0a\u6607\u4e2d\u3067\u3059\u3002\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0\u6559\u80b2\u306e\u73fe\u5834\u3067\u3082C\u306b\u4ee3\u308f\u3063\u3066Python\u306e\u63a1 ..."}, "saleInfo": {"country": "JP", "saleability": "NOT_FOR_SALE", "isEbook": False}, "etag": "bEe3t6nxbxk", "accessInfo": {"webReaderLink": "http://play.google.com/books/reader?id=YVTijgEACAAJ&hl=&printsec=frontcover&source=gbs_api", "publicDomain": False, "embeddable": False, "country": "JP", "textToSpeechPermission": "ALLOWED", "pdf": {"isAvailable": False}, "quoteSharingAllowed": False, "viewability": "NO_PAGES", "epub": {"isAvailable": False}, "accessViewStatus": "NONE"}, "id": "YVTijgEACAAJ", "selfLink": "https://www.googleapis.com/books/v1/volumes/YVTijgEACAAJ"}], "kind": "books#volumes"}
        self.book_empty_detail = {"kind":"books#volumes","totalItems":1,"items":[{"kind":"books#volume","id":"Kt_QuQEACAAJ","etag":"8/JzSs9cUcw","selfLink":"https://www.googleapis.com/books/v1/volumes/Kt_QuQEACAAJ","volumeInfo":{"title":"\u7279\u96C6\u5B9F\u8DF5\u30B5\u30FC\u30D0\u30EC\u30B9\u0020\u0046\u0069\u0072\u0065\u0062\u0061\u0073\u0065\u5927\u6D3B\u7528\u30B9\u30DE\u30FC\u30C8\u30B9\u30D4\u30FC\u30AB\u30FC","publishedDate":"2018","industryIdentifiers":[{"type":"ISBN_10","identifier":"477419851X"},{"type":"ISBN_13","identifier":"9784774198514"}],"readingModes":{"text":False,"image":False},"pageCount":152,"printType":"BOOK","maturityRating":"NOT_MATURE","allowAnonLogging":False,"contentVersion":"preview-1.0.0","panelizationSummary":{"containsEpubBubbles":False,"containsImageBubbles":False},"language":"ja","previewLink":"http://books.google.co.jp/books?id=Kt_QuQEACAAJ&dq=isbn:9784774198514&hl=&cd=1&source=gbs_api","infoLink":"http://books.google.co.jp/books?id=Kt_QuQEACAAJ&dq=isbn:9784774198514&hl=&source=gbs_api","canonicalVolumeLink":"https://books.google.com/books/about/%E7%89%B9%E9%9B%86%E5%AE%9F%E8%B7%B5%E3%82%B5%E3%83%BC%E3%83%90%E3%83%AC%E3%82%B9_Firebase%E5%A4%A7.html?hl=&id=Kt_QuQEACAAJ"},"saleInfo":{"country":"JP","saleability":"NOT_FOR_SALE","isEbook":False},"accessInfo":{"country":"JP","viewability":"NO_PAGES","embeddable":False,"publicDomain":False,"textToSpeechPermission":"ALLOWED","epub":{"isAvailable":False},"pdf":{"isAvailable":False},"webReaderLink":"http://play.google.com/books/reader?id=Kt_QuQEACAAJ&hl=&printsec=frontcover&source=gbs_api","accessViewStatus":"NONE","quoteSharingAllowed":False}}]}

        # Make render
        userid = 'ABC123'
        self.params = {
            'latest_lender': unicode(userid),
            'is_lent': False,
            'created_at': self.now,
            'stocked_at': self.now
        }
        self.params['registered_data'] = self.params


    def test_register_director_title_must_much(self):
        registration = RegisterDirector(self.book).build(DataStoreBuilder(self.entity))
        self.assertEqual(unicode(self.book['items'][0]['volumeInfo']['title']), registration['title'])

    def test_rental_director_title_must_much(self):
        rental = RentalDirector(self.book, **self.params).build(DataStoreBuilder(self.entity))
        self.assertEqual(unicode(self.book['items'][0]['volumeInfo']['title']), rental['title'])

    def test_register_director_when_empty_description(self):
        registration = RegisterDirector(self.book_empty_detail).build(DataStoreBuilder(self.entity))
        self.assertEqual(unicode(self.book_empty_detail['items'][0]['volumeInfo']['title']), registration['title'])
