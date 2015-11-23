#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Synthesizing Tasks."""

import os
import pickle


class PickleCache(object):
    """Custom Class."""
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickleCache class.
        Args:
            file_path(str): defaults to 'datastore.pkl'
            autosync(bool): defaults to false
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """Stores key value pairs in PickleCache."""
        self.__data[key] = value
        if self.autosync:
            self.flush()

    def __len__(self):
        """Returns the lenghth of data"""
        return len(self.__data)

    def __getitem__(self, key):
        """Retrieves data."""
        return self.__data[key]

    def __delitem__(self, key):
        """Deletes data."""
        del self.__data[key]
        if self.autosync:
            self.flush()

    def load(self):
        """Loads data."""
        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """Saves data to file."""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
