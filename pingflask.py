from flask import Flask, render_template, request, stream_with_context, Response, redirect, url_for
from subprocess import Popen, PIPE
import os, signal

app = Flask(__name__)

ping_process = None

@app.route("/", methods=["GET", "POST"])
def ping():
    if request.method == "POST":
        ip_address = request.form.get("ip_address")
        if ip_address:
            return render_template("index.html", ip_address=ip_address)
    return render_template("index.html", ip_address=None)

@app.route("/ping_progress")
def ping_progress():
    global ping_process
    ip_address = request.args.get("ip_address")
    command = ["ping", ip_address]

    def generate():
        global ping_process
        ping_process = Popen(command, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True)
        try:
            for line in iter(ping_process.stdout.readline, ''):
                yield f"data: {line}<br>\n\n"
        except Exception as e:
            yield f"data: An error occurred: {str(e)}<br>\n\n"
        finally:
            ping_process.stdout.close()

    return Response(stream_with_context(generate()), content_type='text/event-stream')

@app.route("/cancel", methods=["POST"])
def cancel_ping():
    global ping_process
    if ping_process:
        os.kill(ping_process.pid, signal.SIGTERM)
        ping_process = None
    return redirect(url_for('ping'))

if __name__ == "__main__":
    app.run(debug=True)
