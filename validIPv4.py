import os
import sys
import socket

def is_valid_ipv4(addr):
    valid_address = addr.split('.')

    # for x in valid_address:
    #     print(x)
    #print(len(valid_address))
    if not len(valid_address) == 4:
        print("Panjang lebih dr 4 atau kurang dari 4")
    for valid in valid_address:
        try:
            alamatIP = int(valid)
        except ValueError:
            return False
        finally:
            if alamatIP > 255 or alamatIP < 0:
                print("Angka yang anda masukkan lebih kecil dari 0 or lebih besar dari 255")

    return True

def valid_to_ip(addr):
    if is_valid_ipv4(addr):
        return addr
    
    try:
        socket.gethostbyname(addr)
    except socket.gaierror:
        print("ping: unknown host %s" % addr)
    finally:
        alamatIP = socket.gethostbyname(addr)
        print(alamatIP)
    # try:
    #     socket.gethostbyname(addr)
    # except socket.gaierror:
    #     print("Your IP address input isn't valid address %s" % addr)
    #     sys.exit(2)
    # finally:
    #     return socket.gethostname(addr)


if __name__ == '__main__':
    # address = sys.argv[1]
    valid_to_ip("192.254.1.2")
    # is_valid_ipv4("192.168.1.1")