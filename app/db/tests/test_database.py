from unittest.mock import patch

import pytest

from app.db.database import Database, StorageError


class Foo:
    def __init__(self):
        self.hello = 1

    def __call__(self):
        None


@patch("app.db.database.scoping.scoped_session")
@patch("app.db.database.sqlalchemy.create_engine")
def test_database(create_engine, session):
    create_engine.return_value = {}
    session.return_value = Foo
    connection = "test"
    new_db = Database(connection)
    assert create_engine.call_count == 1
    assert session.call_count == 1

    with pytest.raises(StorageError):
        new_db.setup()

    assert new_db.session.hello == 1
