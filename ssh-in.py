import paramiko

hostname = 'remote_address'
username = 'root'
password = 'amanaja'
port = 22

try:

    #creating ssh client

    ssh = paramiko.SSHClient
    #Automatically add the server's host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    #Connect to remote hosts
    ssh.connect(hostname,username,password)
    #Get stdin, stdout, and stderr
    stdin, stdout, stderr = ssh.exec_command('ls -lah')
    #Read the output
    print(stdout.read().decode())
    ssh.close()

except paramiko.AuthenticationException:
    print("Error Authentication")

except paramiko.SSHException as ssh_exeption:
    print(ssh_exeption)

