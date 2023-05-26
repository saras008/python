import subprocess

cli = subprocess.run(['ls', '-lah'],stdout=subprocess.PIPE,)

#print('returncode:', cli.returncode)
print(' {} bytes in stdout:\n{}'.format(len(cli.stdout), cli.stdout.decode('utf-8')))
