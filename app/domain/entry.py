class Entry:
    def __init__(self, title, text, tags=None, entry_id=None):
        self.title = title
        self.text = text
        self.tags = tags
        self.entry_id = entry_id


    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if value is None:
            self._tags = None
        elif isinstance(value, (list, tuple, set)):
            self._tags = value
        else:
            self._tags = value.split(',')

        return self
