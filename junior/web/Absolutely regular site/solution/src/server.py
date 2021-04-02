from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from random import randint

NAMES = ['Tom Nook', 'Isabelle', 'K.K. Slider', 'Bill and Ketchup', 'Blanche', 'Drake', 'Jay']
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def main():
    number = randint(1, 7)
    return render_template('index.html', pic=f'picture{number}.jpg', name=NAMES[number - 1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25001)
