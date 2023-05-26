from flask import Flask
from subprocess import check_output

app = Flask(__name__)

@app.route("/ping/<ip_address>")
def ping(ip_address):
    """Pings an IP address and returns the results."""
    command = ["ping", ip_address]
    output = check_output(command).decode("utf-8")
    return output

if __name__ == "__main__":
    app.run()
