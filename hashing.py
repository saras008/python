import os
import hashlib
import sys
import click

@click.group()

@click.option('--method',help='Type your your method',default='md5')

@click.command(get_check_sum)

def get_check_sum(filename,method='md5',block_size=65536):
    try:
        file=os.path.exists(filename)
        return filename
    except:
        raise RuntimeError("Can't open file or dirs no such a file or dirs", filename)
    
    finally:
        if 'sh1' in method:
            checksum = hashlib.sha1()
        elif 'sh256' in method:
            checksum = hashlib.sha256()
        elif 'md5' in method:
            checksum = hashlib.md5()
        else:
            raise RuntimeError("Not supported method %s", method)
        
        with open(filename, 'rb') as file:
            bufering = file.read(block_size)
            while len(bufering) > 0:
                checksum.update(bufering)
                bufering = file.read(block_size)
                if checksum is not None:
                    return checksum.hexdigest()
                else:
                    return checksum 
    
        
def md5sum(filename):
    return get_check_sum(filename)
def sh1sum(filename):
    return get_check_sum(filename,method='sh1')
def sh256sum(filename, method='sh256'):
    print(get_check_sum(filename,method='sh256'))


if __name__ == '__main__':
    filename=sys.argv[1]
    md5sum(filename)
    sh1sum(filename)
    sh256sum(filename)

# print(sh1sum("/Users/saras008/repo-iyus/python/tryexcept.py"))

