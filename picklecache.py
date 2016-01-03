#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pickle """
import os
import pickle

class PickleCache(object):
    """ Class example """

    def __init__(self, file_path='datastore.pkl', autosync=False):
        self.__file_path = file_path
        self.__data = {}
        self.__file_object = None
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        self.__data.update({key:value})
        if self.autosync == True:
            self.flush()
            
    def __len__(self):
        return len(self.__data)
    
    def __getitem__(self, key):
        """Gets data"""
        return self.__data[key]
       
    
    def __delitem__(self, key):
        del self.__data[key]
        if self.autosync == True:
            self.flush()
            
    def load(self):
        """ overloading the method"""
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path):
                fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
   """Saves data to file."""
   fhandler = open(self.__file_path, 'w')
   pickle.dump(self.__data, fhandler)
   fhandler.close()

