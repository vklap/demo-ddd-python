class Entry:
    def __init__(self, title, text, tags=None, entry_id=None):
        self.title = title
        self.text = text
        self.tags = tags
        if tags is None:
            self.tags = None
        else:
            self.tags = tags.split(',')
        self.entry_id = entry_id
