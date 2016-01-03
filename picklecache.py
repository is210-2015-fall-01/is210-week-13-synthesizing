#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will create an object. Get, set, and delete other pickled."""


import os
import pickle


class PickleCache(object):
    """A class. Reads pickle."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """PickleCache class constructor
        Args:
            file_path(str): defaults to datastore.pkl
            autosync(bool): defaults to F
        Attrib:
            __file_path(str): contructor variable
            __data (dict): psuedo-private
            autosync
        Examples:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.__file_object = None
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Cache data behave like dictionary.
        Args:
            key(str): required
            value(str): required
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Gives length of data
        Examples:
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """Retrieve data from obj and handlers when not found.
        Args:
            key(str, required)
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        return self.__data[key]

    def __delitem__(self, key):
        """Removes unwanted obj.
        Args:
            key (str): required
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
        """Loads file object and save contents"""
        if os.path.exists(self.__file_path)\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """Save stored data to file"""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
