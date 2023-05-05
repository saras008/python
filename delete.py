import os

if os.path.exists("test2.txt"):
    os.remove("test2.txt")
    print("File berhasil dihapus")
else:
    print("File didn't exist")