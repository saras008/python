from flask import Flask, render_template, request, send_file, make_response
from flask_wtf.csrf import CSRFProtect
from passlib.hash import bcrypt, md5_crypt, sha1_crypt
import io
import os
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', os.urandom(24))
csrf = CSRFProtect()
csrf.init_app(app)

class HtpasswdForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    algorithm = SelectField('Hashing Algorithm', choices=[('sha1', 'SHA1 (default)'),('bcrypt', 'Bcrypt'), ('md5', 'MD5')])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = HtpasswdForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        algorithm = form.algorithm.data

        # Generate htpasswd entry
        if algorithm == 'bcrypt':
            hashed_password = bcrypt.hash(password)
        elif algorithm == 'md5':
            hashed_password = md5_crypt.hash(password)
        elif algorithm == 'sha1':
            hashed_password=sha1_crypt.hash(password)
        else:
            return render_template('index.html', form=form, error="Hashing algorithm tidak disupport")

        ht_entry = f"{username}:{hashed_password}"

        # Provide option to download as file
        if 'download' in request.form:
            return send_file(
                io.BytesIO(ht_entry.encode()),
                mimetype='text/plain',
                as_attachment=True,
                download_name='.htpasswd'
            )
        return render_template('index.html', form=form, result=ht_entry)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)