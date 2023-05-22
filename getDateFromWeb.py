import requests
import urllib
import datetime
import certifi
import time


host = 'https://www.detik.com'
req = urllib.request.Request(host)

response = urllib.request.urlopen(req,timeout=10)

date = response.getheader("Date")
print(date)

time_header = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')


print(time_header.now())

print(time.strftime('%Y-%m-%d %H:%M:%S', time_header.now().timetuple()))