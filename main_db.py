from flask import Flask
from data import db_session
from data.users import User, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
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

    print()
    for user in db_sess.query(User).all():
        print(user)
    print()
    # app.run()


if __name__ == '__main__':
    main()