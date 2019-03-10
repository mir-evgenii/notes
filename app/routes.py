# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', content='Главная страница.', user='user')

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/reg')
def reg():
    return render_template('reg.html', title='Регистрация', content='Страница регистрации.')

@app.route('/add')
def add():
    return render_template('add.html', title='Создание заметки', content='Создание заметки.', user='user')

@app.route('/edit')
def edit():
    return render_template('edit.html', title='Изменение заметки', content='Изменение заметки.', user='user')

