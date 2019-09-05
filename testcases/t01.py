#!/bin/env python36
# filename: test.py
# Author: lufei
# Date: 20190829 13:11:35

#import sys
#sys.path.insert(0, '..')
#import base

import sys
sys.path.insert(0, '/home/sb/projects/')

from ssautotest import test

class A(test.Testcase):
  name = 'a'

