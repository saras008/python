#!/usr/bin/python

import ntplib
import time
from time import ctime


waktu = ntplib.NTPClient()

respon = waktu.request('pool.ntp.org')


print("current offset time: {}".format(respon.offset))
print("current server time {}".format(ctime(respon.tx_time)))