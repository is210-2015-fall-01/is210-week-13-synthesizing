#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Synthesizing tasks Week 13"""

import os
import pickle


class PickleCache(object):
    """A new Class."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor.

        args:
            file_path (string, optional : Defaults to datastore.pkl.
            autosync (bool, optional) : Defaults to False

        Atr:
         __file_path (string): Pseudo-private attribute assigned to the file_path
         value.
         __data (dict): Pseudo-private attribute.
        autosync: Non-private attribute assigned.

        Returns:
            None.

        Examples:
            >>> cacher = PickleCache()
            >>> print cacher._PickleCache__file_path
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

    def __setitem__(self, key, values):
        """Makes cache behave like a dictionary.

        Args:
            keys : keys for dictionary.
            value : values to be store in dictioary.

        Return:
            None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """

        try:
            self.__data[key] = values
            if self.autosync is True:

                self.flush()
        except (TypeError, KeyError) as error:
            raise error

    def __len__(self):
        """Function returns the length of self.__data.

        Returns:
            Retruns the length of self.__data

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> len(pcache)
            1
        """

        return len(self.__data)

    def __getitem__(self, key):
        """Function uses key to return the requested value from the self.__data
        dictionary.

        Argd:
            key (required) : key used to get items in the dictionary.

        Return:
            Returns the requested value in self.__data dictionary.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """

        return self.__data[key]

    def __delitem__(self, key):
        """Function uses key attribute to remove any entries from the __data
        attribute with the same key.
        
        Args:
            key (mix):  key used to delete entries from the __data attribute.

        Returns:
            None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """

        if self.__data[key]:
            del self.__data[key]
            if self.autosync is True:
                self.flush()

    def load(self):
        """Function for opening and reading file.

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
        loadfile = self.__file_path
        if os.path.exists(loadfile) and os.path.getsize(loadfile) > 0:
            filedata = open(self.__file_path, 'r')
            self.__data = pickle.load(filedata)
            filedata.close()

    def flush(self):
        """uses the pickle.dump() method and the file object close() methods to
        save stored data when commanded to do so.

        Args:
            filedata : file to write and save data to.

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

        filedata = open(self.__file_path, 'w')
        self.__file_object = filedata
        pickle.dump(self.__data, self.__file_object)
        filedata.close()

