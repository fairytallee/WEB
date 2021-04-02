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


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['Инженер', 'Строитель', 'Врач', 'Пилот', 'Ленин', 'Гастроинтеролог', 'Повар', 'Картограф', 'Спецагент',
             'Юрий Дудь', 'Метеоролог', 'Киберинжинер', 'Пилот дронов', 'Климатолог', 'Астрогеолог',
             'Петров', 'экзобиолог', 'Денис Тарков']
    return render_template('list_prof.html', list=list, profs=profs)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=43324)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
