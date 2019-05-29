import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

SAModel = declarative_base()


class Users(SAModel):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), unique=True)

    def __init__(self, name):
        self.name = name

    @property
    def as_dict(self):
        return {"Name": self.name}

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session):
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models
