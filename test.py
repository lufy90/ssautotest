#!/bin/env python36
# filename: test.py
# Author: lufy
# Date: 20190830 22:11:41

import time

class Test():
  '''test class'''
  name = ''
  start_time = ''
  end_time = ''
  testcase = None
  host = None

  def start(self):
    self.start_time = time.time()
  def end(self):
    self.end_time = time.time()
  def get_result(self):
    pass


class Testcase():
  pass
