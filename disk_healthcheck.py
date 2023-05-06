import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100

    return free > 20

check_disk_usage("/")