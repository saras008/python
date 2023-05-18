import os
import sys
from urllib.parse import urlparse


def get_domain_from_url(naming):
    parsing_url = urlparse(naming)
    domain_name = "{uri.netloc}".format(uri=parsing_url)
    if domain_name != "":
        return domain_name
    else:
        return naming.strip().split("/")[0]

# get_domain_from_url("https://stackoverflow.com/questions/9626535/get-domain-name-from-url")

def run_ping(destination,option):
    os_type = sys.platform
    if os_type == 'win32':
        command = "ping.exe {} {}".format(destination,option)
    if os_type == 'linux':
        command = "ping {} {}".format(destination,option)
    else:
        command = "ping {} {}".format(destination,option)
    try:
        os.system(command)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    domainname = sys.argv[1]
    dest=get_domain_from_url(domainname)
    run_ping(dest, "-c4")