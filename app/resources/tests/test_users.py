from unittest.mock import patch

import pytest
from falcon import testing
from sqlalchemy.exc import IntegrityError

from app.app import create_app


class MockSession:
    pass


class MockDB:
    def __init__(self):
        self.session = MockSession()

    def setup(self):
        pass

    def save(self):
        return True


class MockDBBroken:
    def save(self):
        raise IntegrityError({}, {}, {})


@pytest.fixture()
def client():
    mock_db = MockDB()
    mock_db.setup()
    return testing.TestClient(create_app(mock_db))


@patch("app.resources.users.models.Users.get_list")
def test_get_message(get_list_mock, client):
    get_list_mock.return_value = {}
    doc = {"users": {}}

    result = client.simulate_get("/users")
    assert result.json == doc


@patch("app.resources.users.models.Users")
def test_post_message(mock_users, client):
    mock_users.return_value = MockDB

    result = client.simulate_post(
        "/users", headers={"authorization": "yes"}, body='{"name": "bob"}'
    )
    assert result.json is True
    assert mock_users.call_count == 1
    assert mock_users.call_args[1] == {"name": "bob"}


@patch("app.resources.users.models.Users")
def test_post_message_exception(mock_users, client):
    mock_users.return_value = MockDBBroken
    test = client.simulate_post("/users", headers={"authorization": "yes"}, body='{"name": "bob"}')
    assert test._status_code == 400
