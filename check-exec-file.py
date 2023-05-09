#!/usr/bin/python
import os
import sys

def LinuxOrWindows():
    if 'posix' in os.name:
        os_type="Linux"
    elif 'nt' in os.name:
        os_type="Windows"
    else:
        os_type="Others"
    return os_type

def IsWindows():
    if "Windows" in LinuxOrWindows().lower():
        return True
    else:
        return False
    
def IsLinux():
    if "Linux" in LinuxOrWindows().lower():
        return True
    else:
        return False

def ExeFile(path):
    return os.path.isfile(path) and os.access(path,os.X_OK)

def which(path):
    if isinstance(path,str):
        pass
    else:
        return None
    
    fpath, fname = os.path.split(path)

    if fpath:
        if ExeFile(path):
            return path
    else:
        if IsWindows():
            if not path.endswith(".exe"):
                command = path + ".exe"
            else:
                command = path
        else:
            command = path
    return ""

if __name__ == "__main__":
    print(which("ping"))
