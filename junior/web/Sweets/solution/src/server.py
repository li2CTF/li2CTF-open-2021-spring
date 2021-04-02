from flask import Flask, render_template, request, make_response
from random import choice
import base64
# took this template from https://www.free-css.com/free-css-templates/page233/business-casual

app = Flask(__name__, static_url_path='/static')
ALPH = [chr(c) for c in range(ord('a'), ord('z') + 1)] + [chr(c) for c in range(ord('A'), ord('Z') + 1)] + [chr(c) for c in range(0, 10)]
FLAG = b'flag{1_w4nn4_347_50m3_C00k135_w1th_734}'


def random_key() -> str:
    data = []
    for i in range(20):
        data.append(choice(ALPH))
    return ''.join(data)


app.config['SECRET_KEY'] = random_key()


@app.route('/', methods=['GET'])
def main():
    resp = make_response(render_template('index.html'))
    if not request.cookies.get('secret'):
        resp.set_cookie('secret', base64.b64encode(FLAG))
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25002)
