from app.domain.entry import Entry
from app.infrastructure.repositories import connect_db


def get_entries():
    with connect_db() as db:
        cur = db.execute('select title, text from entries order by id desc')
        entries = [Entry(title=row[0], text=row[1]) for row in cur.fetchall()]
        return entries


def add_entry(entry):
    with connect_db() as db:
        db.execute('insert into entries (title, text) values (?, ?)', [entry.title, entry.text])
        db.commit()
