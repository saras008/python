import psutil
import sys
import time

boot_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(psutil.boot_time()))
present = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(boot_time)
print(present)
uptime = time.time() - psutil.boot_time()
days_uptime = int(uptime / 24 / 60 / 60)
hours_uptime= int(uptime / 60 / 60 % 24)
minute_uptime=int(uptime / 60 % 60)
second_uptime=int(uptime % 60)

print("The server already run for %d day, %d hours, %d minute and %d seconds" % (days_uptime,hours_uptime,minute_uptime,second_uptime))

print(psutil.users())

for user in psutil.users():
    username = user[0]
    terminal=user[1]
    login_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(user[3]))
print("User %s login to server at %s on %s" % (username,login_time,terminal))