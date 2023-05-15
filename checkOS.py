#!/usr/bin/env python
import sys
def checkOS():
    if 'posix' in sys.builtin_module_names:
        os_type='Linux'
        print(os_type)

    if 'nt' in sys.builtin_module_names:
        os_type='Windows'
        print(os_type)

    else:
        return 'Others'

checkOS()

def checkDistro():
    with open('/etc/issue','r') as file:
        distro = file.read().lower().strip().split(' ')[0]
        print(distro)

checkDistro()