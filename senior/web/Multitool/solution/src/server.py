from flask import Flask, render_template, request, redirect, url_for, flash, make_response, Flask
from flask_wtf import FlaskForm
import wtforms
import subprocess

app = Flask(__name__, static_url_path='/static')
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
app.config['WTF_CSRF_ENABLED'] = False


class LoginForm(FlaskForm):
    date = wtforms.SubmitField('Date')
    random = wtforms.SubmitField('Cal')
    uptime = wtforms.SubmitField('Uptime')


@app.route('/', methods=['GET', 'POST'])
def main():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        cmd = None
        if form.date.data:
            cmd = form.date.raw_data[0].lower()
        elif form.random.data:
            cmd = form.random.raw_data[0].lower()
        elif form.uptime.data:
            cmd = form.uptime.raw_data[0].lower()
        print(f"[*] Executing: {cmd}")
        result = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
        print(f"[*] Result: {result.stdout[:96 if len(result.stdout) >= 97 else None]}...")
        return render_template('output.html', output=result.stdout.decode("ascii"))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25004)
