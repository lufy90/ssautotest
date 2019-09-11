#!/bin/env python36
# filename: t0001.py
# Author: lufei
# Date: 20190909 13:31:20


import sys,os

p = os.getcwd().split('ssautotest')[0]
sys.path.insert(0,p)

from ssautotest import test

class F(test.Testcase):
  pass
