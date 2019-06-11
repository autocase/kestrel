import logging
from wsgiref import simple_server

import falcon
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from falcon_apispec import FalconPlugin

from app.db.database import Database
from app.environment import create_connection
from app.middleware.auth import AuthMiddleware
from app.middleware.json import RequireJSON, JSONTranslator
from app.routes import build_routes


def application(env, start_response):
    set_logging()
    # Build an object to manage our db connections.
    db = Database(create_connection())
    db.setup()

    app = create_app(db)

    return app(env, start_response)


def create_app(db):
    """

    Args:
        db:

    Returns:

    """
    app = falcon.API(middleware=[AuthMiddleware(), RequireJSON(), JSONTranslator()])

    # Set up documentation object
    spec = APISpec(
        title="Kestrel",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[FalconPlugin(app), MarshmallowPlugin()],
    )
    spec.components.security_scheme("BearerAuth", {"type": "http", "scheme": "bearer"})

    # Build routes
    build_routes(db, app, spec)

    return app


def set_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


# Useful for debugging problems in your API; works with pdb.set_trace().
if __name__ == "__main__":
    httpd = simple_server.make_server("127.0.0.1", 8000, application)
    httpd.serve_forever()
