import sqlite3

from app import app
from contextlib import contextmanager


@contextmanager
def connect_db():
    db = sqlite3.connect(app.config['DATABASE'])
    try:
        yield db
    finally:
        if db is not None:
            db.close()