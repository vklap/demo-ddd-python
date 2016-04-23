import logging

from app.domain.entry import Entry
from app.domain.services import extract_tags
from app.infrastructure.repositories import entries as entries_repo

_log = logging.getLogger(__name__)

def handle_set_tags_for(entry_id):
    try:
        entry = entries_repo.get_entry_by_id(entry_id)

        tags = extract_tags(entry.text)

        entries_repo.update_entry_tags(entry_id, tags)

        _log.info('handle_fill_tags_for entry_id=%s succeeded', entry_id)
    except Exception as ex:
        _log.error('handle_fill_tags_for entry_id=%s failed due to: %s', entry_id, ex)
        raise
