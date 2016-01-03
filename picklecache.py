#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Combination Assignment"""


import os
import pickle


class PickleCache(object):
    """An object that holds PickleCache data"""

    def __init__(self, filepath='datastore.pkl', autosync=False):
        """A constructor function for PickelCache class.

        Args:
            filepath: A string
            autosync: A boolean value

        Attributes:
            It has three instance attributes;
            self.__file_path = filepath
            self.__data = An empty dictionary
            self.autosync = autosync

        Returns:
            None or an empty dictionary

        Example:
            >>>{}
        """
        self.__file_path = filepath
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """A magic method with two parameters; key and value to add
            data to empty dictionary.

        Args:
           key(mixed): key of a dictionary
           value(mixed): value of a dictionary

        Returns:
            string or an integer

        Example:
            >>> pcacahe = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """A magic method.

        Returns:
            int: The length of an object

        Example:
            >>> pcacahe = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """A Python magic method used to get an item.

        Args:
           key(mixed): key of a dictionary

        Returns:
            returns the requested value of a key

        Example:
            >>> pcacahe = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        value = self.__data[key]
        if value is None:
            raise TypeError
        return value

    def __delitem__(self, key):
        """A Python magic method used to delete an item.

        Args:
           key(mixed): Could be an integer or a string

        Example:
            >>> pcacahe = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """
        if key in self.__data:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """A function to use pickle.

        Attributes:
            pickle_file: used to open file and read data
            self.__data: to load data
        """
        if os.path.exists(self.__file_path) \
           and os.path.getsize(self.__file_path) > 0:
            pickle_file = open(self.__file_path, 'r')
            self.__data = pickle.load(pickle_file)
            pickle_file.close()

    def flush(self):
        """A function to dump data.

        Attributes:
            pickle_file: used to open file and write data

        """
        pickle_file = open(self.__file_path, 'w')
        pickle.dump(self.__data, pickle_file)
        pickle_file.close()
