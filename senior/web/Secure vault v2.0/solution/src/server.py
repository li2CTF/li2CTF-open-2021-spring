from flask import Flask, url_for, request, render_template
from flask_wtf import FlaskForm
import wtforms
import threading
from reinit_db import reinit
import random
import sqlite3


DATABASE_NAME = 'vault.db'
DEFAULT = "Empty storage."
USER = "Booo, very-very secret data!"
FLAG = "flag{4b50lu73ly_53cur3_v4ul7_y34h}"
ADMIN = "All secrets moved to sultanowskii"
ALPH = [chr(c) for c in range(ord('a'), ord('z') + 1)] + [chr(c) for c in range(ord('A'), ord('Z') + 1)] + [chr(c) for c in range(0, 10)]


def random_key() -> str:
    data = []
    for i in range(12):
        data.append(random.choice(ALPH))
    return ''.join(data)


app = Flask(__name__)
app.config['SECRET_KEY'] = random_key()
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
app.config['WTF_CSRF_ENABLED'] = False


def timer_reinit():
    threading.Timer(120.0, timer_reinit).start()
    print("[.] Reinited db")
    reinit()


class LoginForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField('Password', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Login')


def check_username(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    try:
        c.execute('SELECT username FROM users WHERE username=(?)', (username,))
    except Exception as e:
        return False
    if c.fetchone():
        return True
    return False


def check_password(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    try:
        c.execute(f'SELECT password FROM users WHERE username=(?) and password=\'{password}\'', (username,))
    except Exception as e:
        print(e)
        return False
    print(f'[.] Now executing: SELECT password FROM users WHERE username=\'{username}\' and password=\'{password}\'')
    if c.fetchone():
        return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        if form.username.data == "sultanowskii" and ("\"" in form.password.data or " " in form.password.data or "OR" in form.password.data or "or" in form.password.data or "1" in form.password.data):
            return render_template('index.html', form=form, error="Nah, we don't like hackers here.")
        if form.username.data == "admin" and ("\"" in form.password.data or "OR" in form.password.data):
            return render_template('index.html', form=form, error="Nah, we don't like hackers here.")
        if not check_username(form.username.data):
            return render_template('index.html', form=form, error="Login doesn't exist.")
        if not check_password(form.username.data, form.password.data):
            return render_template('index.html', form=form, error="Incorrect password.")
        if form.username.data == "sultanowskii":
            print(f"[!] Entered admin storage with password={form.password.data}")
            return render_template('vault.html', data=FLAG)
        elif form.username.data == "user":
            return render_template('vault.html', data=USER)
        elif form.username.data == "admin":
            return render_template('vault.html', data=ADMIN)
        else:
            return render_template('vault.html', data=DEFAULT)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    print("[*] Server is ready!")
    timer_reinit()
    app.run(host='0.0.0.0', port=25003)
    