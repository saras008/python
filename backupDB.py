import os
import paramiko
from subprocess import call
import time
import tarfile

backup_config={
    "user":"root",
    "password":"",
    "host":"",
    "port":"",
    "database":"",
    "backup_dir":"",
    "save_copies":"",
    "save_days":"",
    "storage":{
        "host":{
            "user":"root",
            "password":"",
            "public_key":"",
            "ip":"",
            "ssh_port":"",
            "target":""
        },
        "s3":{},
        "oss":{},
    }
}

def preparation():
    backup_dir = backup_config.get("backup_dir")
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

def compress_file(name,path):
    with tarfile.open(name,'w:gz') as tar:
        try:
            tar.add(path,arcname=os.path.basename(path))
        except tarfile.CompressionError:
            return tarfile.CompressionError
        
def put_file(source,destination):
    host_config = backup_config.get("storage").get("host")
    hostname = backup_config.get("hostname")
    port = int(backup_config.get("ssh_port"))
    username = backup_config.get("user")
    public_key = backup_config.get("public_key")
    timeout = 5

    ssh_client = paramiko.SSHClient()
    #accept missing host key policy
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname,port=port,username=username,key_filename=public_key,timeout=timeout)

    sftp_client = ssh_client.open_sftp()
    sftp_client.put(source,destination)

def backup_mysql():
    cli = """mysqldump -u {user} -p"{password}" -h {host} -p {port} \
    -f -R -E --triggers --single-transaction -B \
    {database} > {backup_dir}/backup_{database}_{now}.sql 2>/dev/null
    """.format(**backup_config)
    call(cli,True)

    backup_filename = "{backup_dir}/backup_{database}_{now}.sql".format(**backup_config)
    tar_backup_name = backup_filename + "tar.gz"
    #compress file with method compress file 
    compress_file(tar_backup_name,backup_filename)

def transfer_file():
    target= backup_config.get("storage").get("host").get("target")
    db = "{backup_dir}/backup_{database}_{now}.sql.tar.gz".format(**backup_config)
    put_file(db,os.path.join(target,os.path.basename(db)))

if __name__ == '__main__':
    preparation()
    backup_mysql()
    transfer_file()

