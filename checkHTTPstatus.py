import os
import requests
import sys
from urllib.parse import urlparse


http_service_config = {
    "name": '',
    "url": 'https://finance.detik.com/',
    "variables": '',
    "headers": '',
    "required_status_code": 200,
}

def check_http():
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.84 Safari/537.36"
    }
    url = http_service_config.get('url')
    required_string = http_service_config.get('required_string')
    required_status_code = http_service_config.get('required_status_code')

    try:
        req = requests.get(url,headers=headers)
    except Exception as e:
        print(e)
        return
    
    status_code = req.status_code

    if status_code == required_status_code:
        status = 'OK'
        match = True
    else:
        status = 'Error'
        match = False
    
    print("Status: {status}\nStatus code: {code}\nKeyword Match:{match}".format(status=status,code=status_code,match=match))

def get_domain_name():
    url = http_service_config.get('url')
    domain = urlparse(url)
    host = domain.netloc
    if ":" in host:
        host,port = host.split(':')
    else:
        if url.startswith('https'):
            port = 443
        else:
            port = 80

    print(host,port)

if __name__ == '__main__':
    check_http()
    get_domain_name()