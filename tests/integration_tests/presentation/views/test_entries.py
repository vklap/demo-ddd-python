import unittest

from tests.integration_tests import AppTestCase

class EntriesTestCase(AppTestCase):
    def test_empty_db(self):
        rv = self.app.get('/')

        self.assertTrue('No entries here so far' in rv.data.decode('utf-8'))


    def test_messages(self):
        self.login(username='admin', password='123456')
        title = 'Hello'
        text = 'DDD is the way to go'
        rv = self.app.post('/add', data=dict(title=title, text=text), follow_redirects=True)

        result = rv.data.decode('utf-8')

        self.assertFalse('No entries' in result)
        self.assertTrue(title in result)
        self.assertTrue(text in result)



