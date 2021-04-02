from flask import Flask
from flask import url_for
from flask import request
from PIL import Image
from io import BytesIO
from flask import render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=43324)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
