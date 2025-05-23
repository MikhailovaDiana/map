from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image():
    return f'''
    <head>
    <title>Колонизация</title>
    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Коланизация</title>
                  </head>
    <h1 style='color:red;'> Жди нас, Марс! </h2>
    <img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
    <div class="alert alert-primary" role="alert"> Человечесво вырасет из детства.</div>
    <div class="alert alert-secondary" role="alert">    Человечеству мала одна планета.</div>
    <div class="alert alert-success" role="alert">    Мы сделаем обитаемыми безжизненные пока планеты.</div>
    <div class="alert alert-warning" role="alert">    И начинаем с Марса!</div>
    <div class="alert alert-danger" role="alert">    Присоединяйся!</div>
    '''



@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Коланизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')