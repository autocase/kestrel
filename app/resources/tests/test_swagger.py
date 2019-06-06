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


def test_get_openapi_spec(client):
    result = client.simulate_get("/api")
    assert result.json['openapi'] == '3.0.2'
