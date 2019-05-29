import falcon
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from app.db import models


class Database:
    """
    Setup the Database connection
    """

    def __init__(self, connection):
        self.connection = connection

        self.engine = sqlalchemy.create_engine(self.connection)
        self.DBSession = scoping.scoped_session(orm.sessionmaker(bind=self.engine, autocommit=True))

    @property
    def session(self):
        return self.DBSession()

    def setup(self):
        try:
            models.SAModel.metadata.create_all(self.engine)
        except Exception as e:
            print("Could not initialize DB: {}".format(e))


class StorageError(Exception):
    @staticmethod
    def handle(ex, req, resp, params):
        description = "Sorry, couldn't write your thing to the " "database. It worked on my box."

        raise falcon.HTTPError(falcon.HTTP_725, "Database Error", description)
