from unittest.mock import patch

import pytest
from falcon import testing

from app.app import create_app


@pytest.fixture()
def client():
    class Object(object):
        pass

    mock_db = Object()
    mock_db.session = {}
    return testing.TestClient(create_app(mock_db))


@patch("app.mail.send_email_to")
def test_get_message(send_email_to, client):
    send_email_to.return_value = {}
    expected = {"email": "success"}

    result = client.simulate_get("/admin")
    assert result.json == expected
