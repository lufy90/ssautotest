#!/bin/env python36
# design.py
# design of this application



objects={
'Test': '',
'Client': '',
}


instance={
'test_inst': '',
}


# execute test in command line
# ./ssauto run -H <hostname> -t <testname,>
# ./ssauto run -H <hostname> -t <testpkg,>
# ./ssauto run -H <hostname> -t <testmodule,>
# ./ssauto run -H <hostname1,hostname2,...> -t <testclass,>
# ./ssauto list
# ./ssauto list -l|--level 1
# ./ssauto list -v
# ./ssauto list <testpkg,>
# ./ssauto list <testmodule,>
# ./ssauto create <testcase,>

# run  -- run test



# case opt is -t:
#   if arg is package:
#     parse package to find all modules, for each module:
#       get all tests inherits from Test class, for each test:
#         execute test
#   if arg is module:
#     get all tests inherits from Test class, for each test:
#       execute test
#   if arg is test:
#     execute test


# HOW ABOUT IF ARGUMENTS OF -t CONFLICTS
# design a priority for what should be run
#   1st priority: test             --  confilict may occure in different modules
#   2nd priority: module           --  confilict may occure in different packages
#   3rd priority: package          --  confilict would not happen

# results collection

# dir tree
# ./
#    - test.py
#    - host.py
#    - libs
#    - ssauto.py
#    - testcases
#      - testpackages
#         - testmodules
#    - scripts
#    - settings.py



