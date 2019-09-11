#!/bin/env python36
# filename: t001.py
# Author: lufy
# Date: 20190908 08:18:01

import sys,os

p = os.getcwd().split('ssautotest')[0]
sys.path.insert(0,p)

from ssautotest import test

class E(test.Testcase):
  pass
