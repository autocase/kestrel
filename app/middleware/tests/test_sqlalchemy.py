from app.middleware.sqlalchemy import SQLAlchemySessionManager


class Resource:
    def __init__(self):
        self.db = DB


class DB:
    def disconnect(self):
        pass


def test_sqlalchemy():
    SQLAlchemySessionManager().process_response(None, None, Resource, None)
