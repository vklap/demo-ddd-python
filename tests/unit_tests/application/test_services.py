import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from app.domain.entry import Entry
from app.application.services import handle_set_tags_for


class TestServices(unittest.TestCase):
    @patch('app.application.services.extract_tags')
    @patch('app.application.services.entries_repo')
    def test_handle_set_tags_for(self, mocked_entries_repo, mocked_extract_tags):
        entry = Entry(title='title 1', text='text 1', entry_id=1)
        extracted_tags = ['tag1', 'tag2']
        mocked_entries_repo.get_entry_by_id.return_value = entry
        mocked_extract_tags.return_value = extracted_tags

        handle_set_tags_for(entry.entry_id)

        mocked_entries_repo.update_entry_tags.assert_called_with(entry.entry_id, extracted_tags)