import unittest

from app.domain.entry import Entry
from app.infrastructure.repositories import entries as repo

from tests.integration_tests import AppTestCase


class EntriesTestCase(AppTestCase):
    def setUp(self):
        super(EntriesTestCase, self).setUp()
        self.entry1 = Entry(title='title1', text='text1')
        self.entry2 = Entry(title='title2', text='text2')

        repo.add_entry(self.entry1)
        repo.add_entry(self.entry2)

    def test_add_and_get_entries(self):
        result = repo.get_entries()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, self.entry2.title)
        self.assertEqual(result[0].text, self.entry2.text)
        self.assertEqual(result[1].title, self.entry1.title)
        self.assertEqual(result[1].text, self.entry1.text)
        self.assertEqual(self.entry1.entry_id, 1)
        self.assertEqual(self.entry2.entry_id, 2)

    def test_update_entry_tags(self):
        tags = ['super', 'great']

        repo.update_entry_tags(self.entry1.entry_id, tags)
        result = repo.get_entry_by_id(self.entry1.entry_id)

        self.assertEqual(result.tags, tags)

    def test_get_entry_by_id(self):
        result = repo.get_entry_by_id(self.entry1.entry_id)

        self.assertIsNotNone(result)
        self.assertEqual(result.text, self.entry1.text)
