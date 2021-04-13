from flask import Flask
from data import db_session
from data.user import User
from data.job import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")


def main3():
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
        user.address = "module_4"
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
    # app.run()


def main4():
    # db_session.global_init("db/mars_explorer.db")
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
        job.is_finished = False
        db_sess.add(job)

    except Exception as ex:
        print(f'Ошибка: {ex}')
    for elem in db_sess.query(Jobs).all():
        print(elem)
    # app.run()


def main5():
    n_base = input('Введите название базы: ')

    try:
        db_session.global_init(f'db/{n_base}')

    except Exception:
        print('Неверное название базы.')
    db_sess = db_session.create_session()
    for elem in db_sess.query(User).all():
        print(elem)


if __name__ == '__main__':
    print()
    print('ЗАДАЧА 3:')
    main3()
    print()
    print('ЗАДАЧА 4:')
    main4()
    print()
    print('ЗАДАЧА 5:')
    main5()
    print()