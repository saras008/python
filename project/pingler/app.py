from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        ip_address = request.form['command']
        ping_output = ping(ip_address)
        #return render_template('result.html',command = ip_address, output=ping_output)
        return render_template('result.html', command=ip_address, output=ping_output)
    return render_template('index.html')
def ping(ip):
    try:
        ouput = subprocess.check_output(['ping','-c', '4',ip])
        return ouput.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(debug=True)
