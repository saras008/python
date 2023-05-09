import requests
import os
import subprocess

req = requests.get("https://www.google.com")

if req.status_code == 200:
    print("Ada koneksi internet")
    print(os.uname())

subprocess.run(["ls","-lah"])
subprocess.run(["ping","1.1.1.1", "-c4"])
