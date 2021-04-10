import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/flag')
def flag():
    return """<img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Flag_of_Tatarstan.svg" />"""

@app.route('/admin')
def admin():
    return """<h4>flag{d1d_y0u_3nj0y_0ur_l0g5?_1_h0p3_y0u_d1d}<h4>"""

@app.route('/<word>')
def random_pic(word):
    w = [360, 480, 600, 720, 960, 1080]
    h = [360, 480, 600, 700]
    width = w[random.randint(0, 5)]
    height = h[random.randint(0, 3)]
    return render_template("li2_for.html", width=width, height=height, word=word)

if __name__ == "__main__":
    # app.debug = True
    app.run()
