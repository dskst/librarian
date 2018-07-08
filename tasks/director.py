# -*- coding: utf-8 -*-
import datetime

class RentalDirector:

    def __init__(self, book, renders):
        self.book = book
        self.renders = renders
        self.now = datetime.datetime.now()

    def build(self, builder):
        builder.add_title(self.book['items'][0]['volumeInfo']['title'])
        builder.add_description(self.book['items'][0]['volumeInfo']['description'])
        builder.add_image_links(self.book['items'][0]['volumeInfo']['imageLinks'])
        builder.add_latest_lender() # TODO:unicode(userid)
        builder.add_is_lent() # TODO:when rental or return
        builder.add_renders() # TODO:render append to response renders
        builder.add_stocked_at() # TODO:stockedAt from response
        builder.add_created_at() # TODO:createdAt from response
        builder.add_updated_at(self.now)
        return builder.get()


class RegisterDirector:

    def __init__(self, book):
        self.book = book
        self.now = datetime.datetime.now()

    def build(self, builder):
        builder.add_title(self.book['items'][0]['volumeInfo']['title'])
        builder.add_description(self.book['items'][0]['volumeInfo']['description'])
        builder.add_image_links(self.book['items'][0]['volumeInfo']['imageLinks'])
        builder.add_is_lent(False)
        builder.add_stocked_at(self.now)
        builder.add_created_at(self.now)
        builder.add_updated_at(self.now)
        return builder.get()