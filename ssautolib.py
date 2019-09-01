#!/bin/env python36
# filename: ssautolib.py
# Author: lufei
# Date: 20190829 10:00:03


import pkgutil
import sys
import importlib
import os
import inspect

def get_sub(pkg_name, sub_modules):
  '''get a list of all modules in pkg_name, sub_modules should be a empty list. '''
  try:
    pkg = importlib.import_module(pkg_name)
    for _, sub_name, ispkg in pkgutil.iter_modules(pkg.__path__):
      if ispkg:
        get_sub(pkg.__name__+'.'+sub_name, sub_modules)
      else:
        sub_modules.append(importlib.import_module(pkg.__name__+'.'+sub_name))

  except Exception as e:
    print(type(e).__name__, e)

def get_subclass(module, baseclass):
  '''get all sub classes of baseclass from module even those in sub modules, 
module is a package object, baseclass is the base class'''
  try:
    if hasattr(module, '__path__'):
      # module is a package object
      sub_modules = []
      get_sub(module.__name__, sub_modules)   # get sub only accept strings.
      sub_class = []
      for mod in sub_modules:
        sub_class.append(get_tests(mod))
      return sub_class
    else:
      return [x for x in vars(module).values() if ssissubclass(x,baseclass)] 
  except Exception as e:
    print(e)
    return []

def ssissubclass(a,b): 
  '''tell if a is subclass of b'''
  try:
    return issubclass(a,b)
  except TypeError:
    return False

def get_module_names_by_path(path='.'):
  '''get a name list of all modules in path, none packages.'''
  if not os.path.isdir(path):
    print('No such directory: %s' % path, file=sys.stderr)
    return -1

  module_names = []
  def _get_module(_path, _prefix, _names):
    for md in pkgutil.iter_modules(path=[_path], prefix=_prefix):
      if md[2]:
        _get_module(os.path.join(_path, md[1]), md[1]+'.', _names)
      else:
         module_names.append(md[1])
  _get_module(path, '', module_names)
  return module_names

def get_modules_by_directory(directory='.'):
  '''get module objects from given directory path'''
  modules = []
  module_names = get_module_names_by_path(directory)
  for n in module_names:
    pkg_spec = importlib.util.spec_from_file_location()
  pass

def get_subclasses_in_module(module_obj, class_obj):
  '''get all subclasses of class_obj in module_obj'''
  subclasses = []
  for i,j in inspect.getmembers(module_obj):
    if ssissubclass(j, class_obj):
      subclasses.append(j)
  return subclasses

# NOT work well
# in importlib.util.spec_from_file_location(module_name, path), module_name
# is just a specified name
def get_subclass_by_module_name(module_name, class_obj, path='./__init__.py'):
  '''get list of sub classes of class_obj in module_name under path'''
  if os.path.isdir(path):
    path = os.path.join(path, '__init__.py')
  spec = importlib.util.spec_from_file_location(module_name, path)
  module_obj = importlib.util.module_from_spec(spec)
  return get_subclasses_in_module(module_obj, class_obj)

