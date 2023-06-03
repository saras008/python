from flask import Flask, render_template, request
import paramiko

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ssh', methods=['POST'])
def ssh():
    hostname = request.form['hostname']
    username = request.form['username']
    password = request.form['password']
    command = request.form['command']

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')

    ssh.close()

    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
