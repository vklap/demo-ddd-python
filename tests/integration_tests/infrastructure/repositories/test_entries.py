import unittest

from app.domain.entry import Entry
from app.infrastructure.repositories import entries as repo

from tests.integration_tests import AppTestCase


class EntriesTestCase(AppTestCase):
    def test_add_and_get_entries(self):
        entry1 = Entry(title='title1', text='text1')
        entry2 = Entry(title='title2', text='text2')

        repo.add_entry(entry1)
        repo.add_entry(entry2)

        result = repo.get_entries()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, entry2.title)
        self.assertEqual(result[0].text, entry2.text)
        self.assertEqual(result[1].title, entry1.title)
        self.assertEqual(result[1].text, entry1.text)
