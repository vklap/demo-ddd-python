import unittest
from unittest.mock import MagicMock

from app.domain.entry import Entry
from app.presentation.views.entries import entries_repo

from tests.integration_tests import AppTestCase

class EntriesTestCase(AppTestCase):
    def test_empty_db(self):
        entries_repo.get_entries = MagicMock(return_value=[])

        rv = self.app.get('/')

        self.assertTrue('No entries here so far' in rv.data.decode('utf-8'))


    def test_add_message(self):
        self.login(username='admin', password='123456')
        title = 'Hello'
        text = 'DDD is the way to go'

        entries_repo.add_entry = MagicMock()

        entry = Entry(title=title, text=text)
        entries_repo.get_entries = MagicMock(return_value=[entry])

        rv = self.app.post('/add', data=dict(title=title, text=text), follow_redirects=True)
        result = rv.data.decode('utf-8')

        saved_entry = entries_repo.add_entry.call_args[0][0]
        self.assertEqual(saved_entry.title, title)
        self.assertEqual(saved_entry.text, text)
        self.assertFalse('No entries' in result)
        self.assertTrue(title in result)
        self.assertTrue(text in result)


    def test_messages(self):
        title = 'Hello'
        text = 'DDD is the way to go'
        entry = Entry(title=title, text=text)
        entries_repo.get_entries = MagicMock(return_value=[entry])

        rv = self.app.get('/')
        result = rv.data.decode('utf-8')

        self.assertFalse('No entries' in result)
        self.assertTrue(title in result)
        self.assertTrue(text in result)



