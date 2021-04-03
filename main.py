from flask import Flask
from flask import url_for
from flask import request
from PIL import Image
from io import BytesIO
from loginform import AstroLoginForm
from flask import render_template
from flask import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    args = {'title': 'Анкета', 'surname': 'Ватник', 'name': 'Алексей', 'education': 'высшее', 'profession': 'Штурман',
            'sex': 'мужской', 'motivation': 'Всегда мечтал умереть!', 'ready': 'ДА!'}
    print(list(args.values()))
    return render_template('auto_answer.html', keys=list(args.keys()), elems=list(args.values()))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AstroLoginForm
    # if form.validate_on_submit():
    #     return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=43324)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
