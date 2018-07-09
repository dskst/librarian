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

    def __init__(self, entity):
        self.entity = entity

    def get(self):
        return self.entity

    def add_isbn(self, isbn):
        self.entity['isbn'] = isbn

    def add_title(self, title):
        self.entity['title'] = unicode(title)

    def add_description(self, description):
        self.entity['description'] = unicode(description)

    def add_image_links(self, image_links):
        self.entity['imageLinks'] = image_links

    def add_is_lent(self, is_lent):
        self.entity['isLent'] = is_lent

    def add_latest_lender(self, latest_lender):
        self.entity['latestLender'] = latest_lender

    def add_renders(self, renders):
        self.entity['renders'] = renders

    def add_stocked_at(self, stocked_at):
        self.entity['stockedAt'] = stocked_at

    def add_created_at(self, created_at):
        self.entity['createdAt'] = created_at

    def add_updated_at(self, updated_at):
        self.entity['updatedAt'] = updated_at


