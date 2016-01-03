#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 syntesizing task."""

import os
import pickle


class PickleCache(object):
    """PickeCache class.

    Attributes
        None
    """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor function for PickleCache class.

        Args:
            file_path(str): a string, defaults to datastore.pkl
            autosync (bool) a boolean, defaults to False.

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
        self.__file_object = None
        self.autosync = autosync
        self.load()

    def __len__(self):
        """a len function.

        Args:
            None
        Returns:
            returns the length of self.__data
        """
        return len(self.__data)

    def __setitem__(self, key, value):
        """This function takes two arguments.
        Args:
            key(str): a key value.
            value(str): a string value.
        Returns:
            None
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        try:
            self.__data[key] = value
            if self.autosync is True:
                self.flush()
        except LookupError:
            raise LookupError

    def __getitem__(self, key):
        """This function returns dict key.
        Args:
            key(str): dict key.

        Returns:
            Retunrs boolean.
        """
        try:
            if self.__data[key]:
                return self.__data[key]

        except LookupError:
            raise KeyError

    def __delitem__(self, key):
        """Delete function.
        Args:
            key(mix): dict key.

        Returns:
            None.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> del pcache['test']
            >>> len(pcache)
            0
        """
        del (self.__data)[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """This function load file.

        Args:
            None.
        Returns:
            None
        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """
        if os.path.exists(self.__file_path) is True\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """This function stored data.
        Args:
            None.
        Returns:
            None
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
