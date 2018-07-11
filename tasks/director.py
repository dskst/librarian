# -*- coding: utf-8 -*-
import datetime

class RentalDirector:

    def __init__(self, book, latest_lender, is_lent, renders, stocked_at, created_at):
        self.book = book
        self.latest_lender = latest_lender
        self.is_lent = is_lent
        self.renders = renders
        self.stocked_at = stocked_at
        self.created_at = created_at
        self.now = datetime.datetime.now()

    def build(self, builder):
        builder.add_title(self.book['items'][0]['volumeInfo']['title'])
        builder.add_description(self.book['items'][0]['volumeInfo']['description'])
        builder.add_image_links(self.book['items'][0]['volumeInfo']['imageLinks'])
        builder.add_latest_lender(self.latest_lender)
        builder.add_is_lent(self.is_lent)
        builder.add_renders(self.renders)
        builder.add_stocked_at(self.stocked_at)
        builder.add_created_at(self.created_at)
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