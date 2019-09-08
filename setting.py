#!/bin/env python36
# filename: setting.py
# Author: lufei
# Date: 20190829 09:49:12

from test import Testcase
import os
import sys

sys.path.insert(0, '/home/sb/projects/')

from ssautotest import test
BASETCASE=test.Testcase


TCASEDIR='testcases'

__all__ = ['BASETCASE', 'TCASEDIR']
