import unittest

from app.domain.entry import Entry

class EntryTestCase(unittest.TestCase):
    def setUp(self):
        self._title = 'title 1'
        self._text = 'text 1'
        self._tags = ['tag1', 'tag2']
        self._entry_id = 1
        self._entry_with_full_data = Entry(title=self._title, text=self._text, tags=self._tags, entry_id=self._entry_id)

    def test_entry_with_full_data(self):
        self.assertEqual(self._entry_with_full_data.title, self._title)
        self.assertEqual(self._entry_with_full_data.text, self._text)
        self.assertEqual(self._entry_with_full_data.tags, self._tags)
        self.assertEqual(self._entry_with_full_data.entry_id, self._entry_id)
