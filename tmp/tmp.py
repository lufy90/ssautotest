#!/bin/env python36

def f0(a, *b, **c):
  print(a)
  print(b)
  print(c)


import argparse
def f1(*a, **b):
  parser = argparse.ArgumentParser(description='test of argpars')
  parser.add_argument('lista', action='store')
  parser.parse_args()



def run(f, *a, **b):
  f(*a, **b)


if __name__ == '__main__':
  run(f1, 'lista', )
