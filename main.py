from flask import Flask
from flask import url_for

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
                        
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}"
                        alt="здесь должна была быть картинка, но не нашлась">
                        
                        <ul>
                            <li>
                                <div class="alert alert-primary" role="alert">
                                    Человечество вырастает из детства.
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-primary" role="alert">
                                    Человечеству мала одна планета.
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-primary" role="alert">
                                    Мы сделаем обитаемыми безжизненные пока планеты.
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-primary" role="alert">
                                    И начнем с Марса!
                                </div>
                            </li>
                            <li>
                                <div class="alert alert-primary" role="alert">
                                    Присоединяйся!
                                </div>
                            </li>
                        </ul>

                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

