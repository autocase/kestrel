class BaseResource:
    def __init__(self, db=None, spec=None):
        self.db = db
        self.spec = spec
