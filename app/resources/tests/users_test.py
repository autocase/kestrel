import json
from unittest.mock import patch

import pytest
from falcon import testing

from app.app import route


@pytest.fixture()
def client():
    class Object(object):
        pass

    mock_db = Object()
    mock_db.session = {}
    return testing.TestClient(route(mock_db))


@patch("app.resources.users.models.Users.get_list")
def test_get_message(get_list_mock, client):
    get_list_mock.return_value = {}
    doc = {"users": []}

    result = client.simulate_get("/users")
    assert result.json == doc
