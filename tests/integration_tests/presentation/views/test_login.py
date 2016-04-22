import unittest

from tests.integration_tests import AppTestCase


class LoginTestCase(AppTestCase):
    def test_login_logout(self):
        rv = self.login(username='admin', password='123456')
        self.assertTrue('You were logged in' in rv.data.decode('utf-8'))

        rv = self.logout()
        self.assertTrue('You were logged out' in rv.data.decode('utf-8'))

    def test_login_failure_given_wrong_credentials(self):
        rv = self.login(username='admin', password='i-am-wrong')
        self.assertTrue('Invalid credentials' in rv.data.decode('utf-8'))



