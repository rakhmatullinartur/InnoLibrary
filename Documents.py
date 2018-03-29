from abc import ABCMeta, abstractmethod, abstractproperty


class Document:
    __metaclass__=ABCMeta
    authors = None
    title = None
    publisher = None


class Book(Document):
    def __init__(self, list_of_authors, publisher, title, edition):
        self.authors = list_of_authors
        self.publisher = publisher
        self.title = title
        self.edition = edition


class JournalArticle(Document):
    def __init__(self, list_of_authors, title, publisher):
        self.title = title
        self.authors = list_of_authors
        self.publisher = publisher


class Media(Document):
    def __init__(self, title, list_of_authors):
        self.title = title
        self.authors = list_of_authors
