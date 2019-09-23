#!/bin/env python36
# filename: test.py
# Author: lufy
# Date: 20190830 22:11:41

import time

class Test():
    '''test class'''
    name = ''
    testcase = None
    host = None
  
    @property
    def start_time_stamp(self):
        return time.time()
    @start_time_stamp.setter
    def start_time_stamp(self, value):
        raise TypeError("Can't set attribute.")
        pass 
    @start_time_stamp.deleter
    def start_time_stamp(self):
        raise AttributeError("Can't delete attribute.")
    def get_result(self):
        pass

class Runingtest():
    pass

class Testcase():
    pass
