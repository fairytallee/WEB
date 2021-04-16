from flask import Flask
from data import db_session
from data.users import User
from data.job import Jobs
from data.news import News
import datetime

from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private is not True)
    return render_template("index.html", news=news, title='Главная')


@app.route("/works_log")
def works_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("works_log.html", jobs=jobs, title='Works Log')


def append_users():
    db_sess = db_session.create_session()
    try:
        db_sess.query(User).delete()
        db_sess.commit()
        user = User()
        user.surname = "Scott"
        user.name = "Ridley"
        user.age = 21
        user.position = "captain"
        user.speciality = "research engineer"
        user.address = "module_1"
        user.email = "scott_chief@mars.org"
        user.hashed_password = "cap"
        db_sess.add(user)
        db_sess.commit()

        user = User()
        user.surname = "Steve"
        user.name = "Jobs"
        user.age = 34
        user.position = "director"
        user.speciality = "all what you want"
        user.address = "module_1"
        user.email = "steve_j@mars.org"
        user.hashed_password = "jobe"
        db_sess.add(user)
        db_sess.commit()

        user = User()
        user.surname = "Elon"
        user.name = "Hask"
        user.age = 51
        user.position = "president"
        user.speciality = "businessman"
        user.address = "module_2"
        user.email = "elon_hasky@mars.org"
        user.hashed_password = "hasky"
        db_sess.add(user)
        db_sess.commit()

        user = User()
        user.surname = "Vlad"
        user.name = "Shmelkov"
        user.age = 16
        user.position = "little gamer"
        user.speciality = "lol"
        user.address = "module_12"
        user.email = "chocolad@mars.org"
        user.hashed_password = "lole"
        db_sess.add(user)
        db_sess.commit()

    except Exception as ex:
        print(f'Ошибка: {ex}')

    for user in db_sess.query(User).all():
        print(user)


def append_jobs():
    db_sess = db_session.create_session()
    try:
        db_sess.query(Jobs).delete()
        db_sess.commit()

        job = Jobs()
        job.team_leader = 1
        job.job = 'deployment of residential modules 1 and 2'
        job.work_size = 15
        job.collaborators = '2, 3'
        job.start_date = datetime.datetime.now()
        job.is_finished = True
        db_sess.add(job)
        db_sess.commit()

        job = Jobs()
        job.team_leader = 4
        job.job = 'работаем над проектом WEB'
        job.work_size = 100000000
        job.collaborators = '1, 4'
        job.start_date = datetime.datetime.now()
        job.is_finished = False
        db_sess.add(job)
        db_sess.commit()

        job = Jobs()
        job.team_leader = 3
        job.job = 'чилит'
        job.work_size = 0
        job.collaborators = '3'
        job.start_date = datetime.datetime.now()
        job.is_finished = False
        db_sess.add(job)
        db_sess.commit()

    except Exception as ex:
        print(f'Ошибка: {ex}')
    for elem in db_sess.query(Jobs).all():
        print(elem)


def main5():
    n_base = input('Введите название базы: ')

    try:
        db_session.global_init(f'db/{n_base}')

    except Exception:
        print('Неверное название базы.')
    db_sess = db_session.create_session()
    for elem in db_sess.query(User).filter(User.address == 'module_1'):
        print(elem)


def append_news():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    try:
        db_sess.query(News).delete()
        db_sess.commit()

        user = db_sess.query(User).filter(User.id == 1).first()
        news = News(title="СЕНСАЦИЯ ВО ВСЕМ ВИНОВАТ НАВАЛЬНЫЙ!!!",
                    content="Сегодня, 16 апреля 2021 года, Алексей Навальный,"
                            " который по официальным данным должен находится"
                            " в местах не столь отадалённых, был заснят на"
                            " камеру грабящим пятёрочку! Попутно он оскорбил"
                            " двух ветеранов! Произвол! Смотреть видео в"
                            " источнике...", is_private=False)
        user.news.append(news)

        user = db_sess.query(User).filter(User.id == 4).first()
        news = News(title="БЕЗОБРАЗИЕ ТАРКОВ!",
                    content="Поиграл в эту вашу escape from tarkov, ужасная игра. Стрельба из оружая вообще не "
                            "понравилась, "
                            " да и геймплей нереалистичный. ВСЕ ЖЕ ЗНАЮТ ЧТО ОТ ТАРКОВА НЕ УБЕЖАТЬ", is_private=False)
        user.news.append(news)

        db_sess.commit()
    except Exception:
        print('Леее брат ошибка')


if __name__ == '__main__':
    append_users()
    append_jobs()
    append_news()
    app.run(port=8080, host='127.0.0.1')