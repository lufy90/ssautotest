Super Simple Autotest for linux
Belongs to ssprojects(Super Simple Projects by Lufei)

An restructured version of sstest/ssautotest
Better designed.



Purpose of ssautotest than `sstest/ssautotest`:
1. With priorities management.
2. Better management about test clients.


Usage:
ssauto run TESTMODULE|TESTPACKAGE 
           [-H HOST][-h|--help][-d|--directory DIRECTORY]
           [-p|--priority N][-t|--test TEST]

ssauto list [TESTPACKAGE|TESTMODULE] 
            [-v|--verbose][-h|--help][-d|--directory DIRECTORY]
            [-p|--priority N]

ssauto create [-h|--help] TESTMODULE

ssauto help
