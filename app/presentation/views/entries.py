from flask import render_template, url_for, redirect, flash, request

from app import app

from app.domain.entry import Entry
from app.infrastructure.repositories import entries as entries_repo
from app.presentation import login_required


@app.route('/')
def show_entries():
    entries = entries_repo.get_entries()
    return render_template('entries/show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
@login_required
def add_entry():
    entry = Entry(title=request.form['title'], text=request.form['text'])
    entries_repo.add_entry(entry)
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


