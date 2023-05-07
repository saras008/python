import requests
from pythonping import ping

def cek_internet():
    request = requests.get("www.google.com")

def pinger():
    pingers=ping('1.1.1.1',count = 3)

pinger()