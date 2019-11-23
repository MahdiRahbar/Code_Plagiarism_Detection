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
        self.valid_format = ['.cpp', '.py', '.ipynb']
        self.doc_dict = {}


    def Load_Data(self):
        '''
        Loading the data from the given path.
        '''
        for filename in os.listdir(self.loading_dir):
            f_name , f_ext = splitext(filename)  
            if f_ext in self.valid_format:
                file_path = self.loading_dir + '/' + filename
                loaded_file = open(file_path,'r',encoding = "utf-8") 
                line_seperated_data = loaded_file.readlines() 
                self.doc_dict[filename] = line_seperated_data[0]
 
        return self.doc_dict

    def Tokenizer(self):
        pass

    