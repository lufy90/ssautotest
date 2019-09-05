Super Simple Autotest for linux
Belongs to ssprojects(Super Simple Projects by Lufei)

An restructured version of sstest/ssautotest
Better designed.



Purpose of ssautotest than `sstest/ssautotest`:
1. With priorities management.
2. Better management about test clients.

```
Usage:
ssauto run TESTMODULE|TESTPACKAGE 
           [-H HOST][-h|--help][-d|--directory DIRECTORY]
           [-p|--priority N][-t|--test TEST]

# 1st design:
ssauto list [TESTPACKAGE|TESTMODULE] 
            [-v|--verbose][-h|--help][-d|--directory DIRECTORY]
            [-p|--priority N][-m|--module]

            -m list all modules
            -v list object detailed doc

# 2nd design:
ssauto list : default list test modules and test classes under DIRECTORY
            [DIRECTORY]
            [-h|--help][-m|--module MODULE]
            [-t|--test TEST][-p|--priority N]
            [-v|--verbose]

  -m specify query test module
  -M only list modules
  -t specify query test class, list test class detail
  -p only list test class with specified priority
  -v list details, about module docs or test docs.


ssauto run DIRECTORY
           [-m|--module TESTMODULE]
           [-t|--test TESTCASE]
           [-H HOST]
           [-p|--priority N]
              
ssauto create [-h|--help] TESTMODULE

ssauto help

```
Examples:
ssauto list -d testcases

1st design:
```
PKG1.MODULE1  : MODULE1DOCS(partly)
  TEST1       : TEST1DOCS(partly)
  TEST2       : TEST2DOCS
  TEST3
PKG2.MODULE2
  TEST4
  TEST5
  TEST6
```
2nd design:
```
PKG1.MODULE1 TEST1 TEST2 TEST3
PKG2.MODULE2 TEST4 TEST5 TEST6
```
