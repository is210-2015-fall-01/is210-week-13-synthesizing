#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1-7"""

import os
import pickle


class PickleCache(object):
    """ class for read pickle file"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """ pickleCache constructor
        args:
        file_path (string, optional) Defaults to datastore.pkl
        autosync (bool, optional) Defaults to False
        Attributes
         __file_path(string): assigned the constructor variable file_path value.
         __data (dict): Pseudo-private attr. and store the data in the file.
        autosync: A non-private attr. assigned the contructor varraible autosync
        Returns:
            None
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
        """ fuction to make our cache behave like a dictionary. and make
            __data attribute accessible to outside objects
        args:
        key (strings): keys of the dict _data
        value (mix): values to be store in the data dict
        return
            None
        example:
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
        """function that deetermine the lenght of dict __data
        returns:
            retruns the length of self.__data
        example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> len(pcache)
            1
        """

        return len(self.__data)

    def __getitem__(self, key):
        """ function to get items in dict __data
        args:
            key (mix): key to use to get the items in the dict
        return:
            return the requested value in self.__data dictionary.
        example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        try:
            if self.__data[key]:
                datakey = self.__data[key]
                if self.autosync is True:
                    self.flush()
            return datakey

        except (TypeError, KeyError) as error:
            raise error

    def __delitem__(self, key):
        """ function to determin and delete entries from the __data
        args:
            key (mix):  key of entries to be delete entries from the __data
        return:
            none
        example:
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
        """ method open and read file
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
        """function to save the data found in the PickleCache __data
        Args:
            filedata (file): the file to write data to
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
