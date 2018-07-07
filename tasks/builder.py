# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Builder:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add_isbn(self, isbn):
        pass

    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_description(self, description):
        pass

    @abstractmethod
    def add_image_links(self, image_links):
        pass

    @abstractmethod
    def add_is_lent(self, is_lent):
        pass

    @abstractmethod
    def add_latest_lender(self, latest_lender):
        pass

    @abstractmethod
    def add_renders(self, renders):
        pass

    @abstractmethod
    def add_stocked_at(self, stocked_at):
        pass

    @abstractmethod
    def add_created_at(self, created_at):
        pass

    @abstractmethod
    def add_updated_at(self, updated_at):
        pass


class DataStoreBuilder(Builder):

    def __init__(self):
        self.data = {}

    def get(self):
        return self.data

    def add_isbn(self, isbn):
        self.data['isbn'] = isbn

    def add_title(self, title):
        self.data['title'] = unicode(title)

    def add_description(self, description):
        self.data['description'] = unicode(description)

    def add_image_links(self, image_links):
        self.data['image_links'] = image_links

    def add_is_lent(self, is_lent):
        self.data['is_lent'] = is_lent

    def add_latest_lender(self, latest_lender):
        self.data['latest_lender'] = latest_lender

    def add_renders(self, renders):
        self.data['renders'] = renders

    def add_stocked_at(self, stocked_at):
        self.data['stocked_at'] = stocked_at

    def add_created_at(self, created_at):
        self.data['created_at'] = created_at

    def add_updated_at(self, updated_at):
        self.data['updated_at'] = updated_at


