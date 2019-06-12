import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from app.session import session_scope

SAModel = declarative_base()


class Users(SAModel):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), unique=True)

    def __init__(self, name):
        self.name = name

    @property
    def as_dict(self):
        return {"name": self.name, "id": self.id}

    def save(self, session):
        with session_scope(session) as se:
            se.add(self)
            our_user = se.query(Users).filter_by(name=self.name).first()
            result = our_user.as_dict
        return result

    @classmethod
    def get_list(cls, session):
        with session_scope(session) as se:
            query = se.query(cls)
            models = query.all()
            users = [model.as_dict for model in models]

        return users
