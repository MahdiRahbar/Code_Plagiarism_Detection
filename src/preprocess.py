# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:52:45 2019

@author: Mahdi
"""
import os 
import re
from os.path import splitext, split


class DataReader():
    """
    
    """
    def __init__(self, loading_dir, saving_dir, fformat):
        self.loading_dir = loading_dir
        self.saving_dir = saving_dir
        self.fformat = fformat   # imported file format
                                # pls note that file format has to be 
                                # double checked in the future to see
                                # if the imported format is valid for 
                                # the application.


    def Load_Data(self):
        pass

    def Tokenizer(self):
        pass

    