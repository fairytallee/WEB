from flask import Flask
from flask import url_for
from flask import request
from PIL import Image
from io import BytesIO
from flask import render_template

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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def two_params(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h1 style="text-align: center; margin-top: 30px; margin-bottom: 30px;">Результаты отбора претендента {nickname} на участие в миссии</h1>

                    <ul class="list-unstyled" style="text-align: center;">
                            <li>
                                <div class="alert alert-success" role="alert" color="green">
                                    <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора:</h3>
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-danger" role="alert">
                                    <h3>{rating} баллов!!!</h3>
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-info" role="alert">
                                    <h3>Желаем удачи!</h3>
                                </div>
                            </li>
                        </ul>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
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
                            <title>Загрузга фото</title>
                          </head>
                          <body>
                            <h1>Загрузка фото</h1>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <ul class="list-unstyled">
                                        <li>
                                            <div class="form-group">
                                                <label for="photo">Приложите вашу фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                        </li>
                                        <li>
                                            <button type="submit" class="btn btn-primary">Отправить фото</button>
                                        </li>
                                    </ul>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        img = Image.open(f)
        print(img)
        return f"""<img src="{url_for(img)}" alt="Картинка" >"""


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
                        <title>Пример с несколькими параметрами</title>
                      </head>
                      <body>
                        <h1 style="text-align: center; margin-top: 30px; margin-bottom: 30px;">Красивый марс...</h1>

                        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                            <ol class="carousel-indicators">
                                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                            </ol>
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img class="d-block w-100" src="{url_for('static', filename='img/mars1.jpg')}" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                    <img class="d-block w-100" src="{url_for('static', filename='img/mars2.jpg')}" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                    <img class="d-block w-100" src="{url_for('static', filename='img/mars3.jpg')}" alt="Third slide">
                                </div>
                                <div class="carousel-item">
                                    <img class="d-block w-100" src="{url_for('static', filename='img/mars4.jpg')}" alt="Fourth slide">
                                </div>
                            </div>
                            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                            </a>
                            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                            </a>
                        </div>

                        <div id="carouselExampleCaptions" class="carousel slide" data-mdb-ride="carousel">
                            <div class="carousel-indicators">
                                <button
                                type="button"
                                data-mdb-target="#carouselExampleCaptions"
                                data-mdb-slide-to="0"
                                class="active"
                                aria-current="true"
                                aria-label="Slide 1"
                                ></button>
                                <button
                                type="button"
                                data-mdb-target="#carouselExampleCaptions"
                                data-mdb-slide-to="1"
                                aria-label="Slide 2"
                                ></button>
                                <button
                                type="button"
                                data-mdb-target="#carouselExampleCaptions"
                                data-mdb-slide-to="2"
                                aria-label="Slide 3"
                                ></button>
                            </div>
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img
                                    src="https://mdbootstrap.com/img/new/slides/041.jpg"
                                    class="d-block w-100"
                                    alt="..."
                                    />
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5>First slide label</h5>
                                        <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img
                                    src="https://mdbootstrap.com/img/new/slides/042.jpg"
                                    class="d-block w-100"
                                    alt="..."
                                    />
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5>Second slide label</h5>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img
                                    src="https://mdbootstrap.com/img/new/slides/043.jpg"
                                    class="d-block w-100"
                                    alt="..."
                                    />
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5>Third slide label</h5>
                                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                                        </div>
                                    </div>
                                </div>
                                <button
                                class="carousel-control-prev"
                                type="button"
                                data-mdb-target="#carouselExampleCaptions"
                                data-mdb-slide="prev"
                                >
                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                    <span class="visually-hidden">Previous</span>
                                </button>
                                <button
                                class="carousel-control-next"
                                type="button"
                                data-mdb-target="#carouselExampleCaptions"
                                data-mdb-slide="next"
                                >
                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                    <span class="visually-hidden">Next</span>
                                </button>
                            </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')