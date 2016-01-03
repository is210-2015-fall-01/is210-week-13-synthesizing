#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring."""


import os
import pickle


class PickleCache(object):
    """PickleCache class for this assignment."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """This is the constructor function.

        The constructor function.

        Args:
            file_path (string): file to save dictionary.
            autosync (boolean): save automatically.

        Attributes:
            self.__file_path = Semi private file_path
            self.__data = Dictionary
            self.autosync = autosync

        Example:
            >>> pcache = PickleCache(autosync=True)
            >>>
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Populates the dictionary.

        This function sets the dictionary with the key/valye pair.

        Attributes:
            key (mixed): Dictionary key
            value (mixed): Dictionary value
            self.autosync = autosync

        Example:
            >>> pcache['apples'] = 'oranges'
            >>>
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __getitem__(self, key):
        """Returns dictionary items.

        This function returns the dictionary item specified by the key.

        Attributes:
            key (mixed): Dictionary key
            self.__data = The dictionary

        Returns:
            The value of the key.

        Example:
            >>> pcache['apples']
            'oranges'
        """
        try:
            if self.__data[key]:
                item = self.__data[key]
                return item
        except (TypeError, KeyError) as err:
            raise err

    def __delitem__(self, key):
        """Detele item.

        This function deletes from a dictionary.

        Attributes:
            key (mixed): Key of a dictionary item to be deleted.
            self.__data = The dictionary.

        Example:
            >>> del pcache['apples']
            >>>
        """
        if key in self.__data:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """The len function.

        Returns length of dictionary.

        Returns:
            len (int): Length of the dictionary.

        Example:
            >>> len(pcache)
            0
        """
        return len(self.__data)

    def load(self):
        """Loads from file.

        This function reads dictionary data from the pickle file.

        Attributes:
            pfile (mixed): File to load dictionay data from.
            self.__data (dictionary): The dictionary.
        """
        if os.path.exists(self.__file_path) and \
           0 < os.path.getsize(self.__file_path):
            pfile = open(self.__file_path, 'r')
            self.__data = pickle.load(pfile)
            pfile.close()

    def flush(self):
        """Flush the dict to file.

        This function flushes the dictionary to the pickle file.

        Attributes:
            pfile (mixed): File to write dictionary data to.
            self.__data (dictionary): The dictionary.
        """
        pfile = open(self.__file_path, 'w')
        pickle.dump(self.__data, pfile)
        pfile.close()
