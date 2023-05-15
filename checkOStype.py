import os
import platform

class OSType(object):
    MacOS =['MacOS']
    Linux=['Linux']

class OSBrand(object):
    OS13=['Ventura']
    centos=['CentOS']


def get_os_type():
    uname = platform.system().strip().strip('"').strip("'").strip().lower()
    if 'linux' in uname:
        os_type = OSType.Linux[0]
        print(os_type)

    if 'darwin' in uname:
        os_type=OSType.MacOS[0]
        print(os_type)

def get_os_brand(os_type):
    dist = platform.system()

    if os_type in OSType.MacOS:
        os_name = platform.mac_ver()[0].strip().strip('"').lower()
        if os_name.startswith('13'):
            return OSBrand.OS13[0]
        
def get_os_info():
    os_type = get_os_type()
    os_brand = get_os_brand(os_type)
    return os_type,os_brand

def main():
    os_type, os_brand = get_os_info()

if __name__ == '__main__':
    main()
