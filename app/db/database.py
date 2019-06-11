import logging

import falcon
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from app.db import models

log = logging.getLogger(__name__)


class Database:
    """
    Setup the Database connection
    """

    def __init__(self, connection):
        """"""
        self.engine = sqlalchemy.create_engine(connection)
        self.db = scoping.scoped_session(
            orm.sessionmaker(bind=self.engine, autocommit=True)
        )

    @property
    def session(self):
        return self.db()

    def setup(self):
        try:
            models.SAModel.metadata.create_all(self.engine)
        except Exception as e:
            log.exception("Could not initialize DB: {}".format(e))
            raise StorageError(Exception)


class StorageError(Exception):
    @staticmethod
    def handle(ex, req, resp, params):
        description = (
            "Sorry, there was a problem with the database, please try again later."
        )
        log.error(description)
        raise falcon.HTTPError(falcon.HTTP_725, "Database Error", description)
