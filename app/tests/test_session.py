import falcon
import pytest
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from falcon_apispec import FalconPlugin

from app.session import session_scope


@pytest.fixture()
def app():
    return falcon.API()


@pytest.fixture()
def spec(app):
    # Set up documentation object
    spec = APISpec(
        title="Test",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[FalconPlugin(app), MarshmallowPlugin()],
    )
    return spec


class mockDB:
    def setup(self):
        return None


def test_session(app, spec):
    session_scope()
