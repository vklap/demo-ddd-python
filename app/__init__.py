import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from functools import wraps

DATABASE = '/tmp/flaskr.db'
DEGUG = True
SECRET_KEY = 'DDD Forever'
USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__, static_folder='presentation/views/static', template_folder='presentation/views/templates')
app.config.from_object(__name__)

from app.presentation import views
from app.presentation.views import entries


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('../scripts/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response):
    return response


@app.teardown_request
def teardown_request(exception):
    pass