#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""wk13 sythnezing tasks 1-7."""


import os
import pickle


class PickleCache(object):
    """A custom class."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for the PickleCache class.
        Args:
            file_path(string): Defaults to datastore.pkl.
            autosync(bool): Defaults to False.
        Example:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """A function that cache data as a dictionary.
        Args:
            key(string): A required input.
            value(string): A required input.
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """

        self.__data[key] = value
        if self.autosync:
            self.flush()

    def __len__(self):
        """A function that checks for the length of the data.
        Example:
            >>> len(pcache)
            1
        """

        return len(self.__data)

    def __getitem__(self, key):
        """A function that retrieves data.
        Args:
            key(string, required): A required input.
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """

        return self.__data[key]

    def __delitem__(self, key):
        """A function that delete items.
        Args:
            key (string): A required input.
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """

        del self.__data[key]
        if self.autosync:
            self.flush()

    def load(self):
        """A function that loads existing file."""

        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """function that writes data to a file."""

        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
