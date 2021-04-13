from flask import Flask, redirect, render_template
from data import db_session
from data.user import User
from data.job import Jobs
from loginform import LoginForm
from flask_login import login_user
import datetime

from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and form.password.data == user.hashed_password:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")

        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


def main3():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    try:
        db_sess.query(User).delete()
        db_sess.commit()
        user = User()
        user.surname = "Илья"
        user.name = "Брыкин"
        user.age = 21
        user.position = "captain"
        user.speciality = "research engineer"
        user.address = "wdf"
        user.email = "bryilyant16@gmail.com"
        user.hashed_password = "12345678"
        db_sess.add(user)
        db_sess.commit()

    except Exception as ex:
        print(f'Ошибка: {ex}')

    for user in db_sess.query(User).all():
        print(user)
#
#
# def main4():
#     # db_session.global_init("db/mars_explorer.db")
#     db_sess = db_session.create_session()
#     try:
#         db_sess.query(Jobs).delete()
#         db_sess.commit()
#         job = Jobs()
#         job.team_leader = 1
#         job.job = 'deployment of residential modules 1 and 2'
#         job.work_size = 15
#         job.collaborators = '2, 3'
#         job.start_date = datetime.datetime.now()
#         job.is_finished = False
#         db_sess.add(job)
#
#     except Exception as ex:
#         print(f'Ошибка: {ex}')
#     for elem in db_sess.query(Jobs).all():
#         print(elem)
#     # app.run()


if __name__ == '__main__':
    main3()
    app.run(port=8080, host='127.0.0.1')