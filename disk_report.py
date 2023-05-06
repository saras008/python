import shutil

du = shutil.disk_usage("/")

print("Your total disk space is ", du)

#persentase disk

print("Free disk space is % : ", du.free/du.total * 100)
