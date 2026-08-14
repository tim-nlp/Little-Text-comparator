class TextReader:
    """A simple class that reads texts."""

    def __init__(self, path):
        self.path = path

    def read_text(self):
        path = self.path
        contents = path.read_text().rstrip()
        return contents