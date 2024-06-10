#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._name.articles=[]

        @property
        def name(self):
            return self._name
        
        def articles(self):
            return [article for article in Article if article.author == self ]
        
        def magazines(self):
            return [article.magazine for article in self.articles()]
        
        def add_articles(magazine, title):
            pass
        

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = name

        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = category

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance.")
        self._author = author

        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        self._magazine = magazine

        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string between 5 and 50 characters.")
        self._title = title

    @property
    def title(self):
        return self._title
