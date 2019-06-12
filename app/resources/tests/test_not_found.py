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


def test_not_found(client):
    rest = client.simulate_get("/asdfg")
    assert rest.status_code == 404
