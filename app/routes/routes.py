from app import app, db
from flask import request, render_template, redirect
import re

from app.models.models import User


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<name>')
def greet(name):
    return render_template('hello.html', user=name)


@app.route('/guest')
def guest():
    return render_template('hello.html', user=None)


@app.route('/age/<int:age>')
def show_age(age):
    return f'Age is {age}!'


# @app.route('/form', methods=['GET', 'POST'])
# def form_handler():
#     if request.method == 'POST':
#         return 'Дані отримано через POST'
#     return 'Це форма (get)'


@app.route('/go_home')
def go_home():
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return 'Сторінку не знайдено', 404


@app.route('/square/<int:number>')
def square(number):
    return f'Square is {number * number}!'


@app.route('/language')
def language():
    langs = ['Python', 'Flask', 'HTML', 'CSS']
    return render_template('lang.html', langs=langs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    name = ''
    email = ''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        if not name:
            error = 'Ім’я не може бути порожнім'
        elif not email:
            error = 'Email не може бути порожнім'
        elif not is_valid_email(email):
            error = 'Email має неправильний формат'
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return f"User {new_user.name} registered successfully!"
    return render_template('form.html', error=error, name=name, email=email)


# @app.route('/form', methods=['GET', 'POST'])
# def contact_form():
#     error = None
#     name = ''
#     email = ''
#
#     if request.method == 'POST':
#         name = request.form.get('name', '').strip()
#         email = request.form.get('email', '').strip()
#
#         if not name:
#             error = 'Ім’я не може бути порожнім'
#         elif not email:
#             error = 'Email не може бути порожнім'
#         elif not is_valid_email(email):
#             error = 'Email має неправильний формат'
#         else:
#             return render_template('form.html', name=name, email=email)
#
#     return render_template('form.html', error=error, name=name, email=email)
