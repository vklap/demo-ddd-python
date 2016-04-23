import sqlite3 as lite
from app.domain.entry import Entry
from app.infrastructure.repositories import connect_db


def get_entry_by_id(entry_id):
    with connect_db() as db:
        db.row_factory = lite.Row
        cur = db.cursor()
        cur.execute('select title, text, tags, id from entries where id=%s' % int(entry_id))
        row = cur.fetchone()
        entry = Entry(title=row['title'], text=row['text'], tags=row['tags'], entry_id=row['id'])
        return entry


def get_entries():
    with connect_db() as db:
        db.row_factory = lite.Row
        cur = db.execute('select title, text, tags, id from entries order by id desc')
        entries = [Entry(title=row['title'], text=row['text'], tags=row['tags'], entry_id=row['id']) for row in cur.fetchall()]
        return entries


def add_entry(entry):
    with connect_db() as db:
        cur = db.cursor()
        cur.execute('insert into entries (title, text) values (?, ?)', [entry.title, entry.text])
        db.commit()
        entry.entry_id = cur.lastrowid


def update_entry_tags(entry_id, tags):
    tags_string = ','.join(tags)
    with connect_db() as db:
        db.execute('update entries set tags=? where id=?', [tags_string, entry_id])
        db.commit()


