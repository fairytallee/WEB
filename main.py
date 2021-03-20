from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def first():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>

                Человечеству мала одна планета.<br>

                Мы сделаем обитаемыми безжизненные пока планеты.<br>

                И начнем с Марса!<br>

                Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}"
                        alt="здесь должна была быть картинка, но не нашлась">
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1 style="color: red; text-align: left;">Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}"
                        alt="здесь должна была быть картинка, но не нашлась">
                        
                        <ul class="list-unstyled">
                            <li>
                                <div class="alert alert-success" role="alert" color="green">
                                    Человечество вырастает из детства.
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-danger" role="alert">
                                    Человечеству мала одна планета.
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-info" role="alert">
                                    Мы сделаем обитаемыми безжизненные пока планеты.
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-warning" role="alert">
                                    И начнем с Марса!
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-secondary" role="alert">
                                    Присоединяйся!
                                </div>
                            </li>
                        </ul>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <ul class="list-unstyled">
                                        <li>
                                            <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="text">
                                        </li>
                                        <li>
                                            <input type="text" class="form-control" id="text" placeholder="Введите имя" name="text">
                                        </li>
                                        <li>
                                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        </li>
                                        <li>
                                            <div class="form-group">
                                                <label for="classSelect">Образование</label>
                                                    <select class="form-control" id="classSelect" name="class">
                                                        <option>начальное</option>
                                                        <option>среднее</option>
                                                        <option>высшее</option>
                                                    </select>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-group">
                                                <label for="form-check">Предполагаемая должность</label>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="prof" id="ing" value="1" checked>
                                                    <label class="form-check-label" for="ing">
                                                        инженер-исследователь
                                                    </label>
                                                </div>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="prof" id="pil" value="2">
                                                    <label class="form-check-label" for="pil">
                                                        пилот
                                                    </label>
                                                </div>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="prof" id="bil" value="3">
                                                    <label class="form-check-label" for="bil">
                                                        строитель
                                                    </label>
                                                </div>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="prof" id="doc" value="4">
                                                    <label class="form-check-label" for="doc">
                                                        врач
                                                    </label>
                                                </div>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="prof" id="cyb" value="5">
                                                    <label class="form-check-label" for="cyb">
                                                        киберинженер
                                                    </label>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-group">
                                                <label for="form-check">Укажите пол</label>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                    <label class="form-check-label" for="male">
                                                        Мужской
                                                    </label>
                                                </div>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                    <label class="form-check-label" for="female">
                                                        Женский
                                                    </label>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-group">
                                                <label for="about">Почему вы хотите участвовать?</label>
                                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-group">
                                                <label for="photo">Приложите вашу фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-group form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Политика конфиденциальности</label>
                                            </div>
                                        </li>
                                        <li>
                                            <button type="submit" class="btn btn-primary">Записаться</button>
                                        </li>
                                    </ul>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def greeting(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора: {planet_name}</title>
                  </head>
                  <body>
                    <h1 style="text-align: center; margin-top: 30px; margin-bottom: 30px;">Моё предложение: {planet_name}!</h1>
                    
                    <ul class="list-unstyled" style="text-align: center;">
                            <li>
                                <div class="alert alert-success" role="alert" color="green">
                                    <h3>Эта планета недалека от земли</h3>
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-danger" role="alert">
                                    <h3>На ней много ресурсов</h3>
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-info" role="alert">
                                    <h3>На планете {planet_name} можно терраформировать воду и атмосферу</h3>
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-warning" role="alert">
                                    <h3>У планеты {planet_name} есть сильное магнитное поле!</h3>
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-secondary" role="alert">
                                    <h3>А также {planet_name} очень красивая планета!</h3>
                                </div>
                            </li>
                        </ul>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
