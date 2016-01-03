#!user/bin/env python
# -*- coding: utf-8 -*-
"""Pickle"""

import os
import pickle


class PickleCache(object):
    """Pickle Class"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor.
        Args:
            file_path (str): defaults to datastore.pkl file
            autosync (bool): defaults to false
        Returns:
            None
        Examples:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Sets variable and key.
        Args:
            key: dict key
            value: dict value
        Returns:
            key/value in dict
        Exxamples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        self.__data[key] = value
        if self.autosync:
            self.flush()

    def __len__(self):
        """Returns len of file.
        Returns:
            Len of ile
        Exmaples:
            >>> len(pcache)
            1
        """
        length = len(self.__data)
        return length

    def __getitem__(self, key):
        """Return value of key.
        Args:
            key: key of dict from __setitem__ method
        Returns:
            Value of key
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        getkey = self.__data[key]
        return getkey

    def __delitem__(self, key):
        """del key if already exists in dict.
        Args:
            key from __setitem__ method
        Returns:
            if key exists, del key
        Examples:
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
        """Opens and loads file to work on.
        Args:
        Returns:
            Opens file to retrieve data
        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                openfile = open(self.__file_path, 'r')
                self.__data = pickle.load(openfile)
                openfile.close()

    def flush(self):
        """Saves information to file.
        Args:
        Returns:
            Saves information to file
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        openfile = open(self.__file_path, 'w')
        pickle.dump(self.__data, openfile)
        openfile.close()
