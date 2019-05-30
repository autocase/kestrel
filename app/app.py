import logging
import os
from wsgiref import simple_server

import falcon
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from falcon_apispec import FalconPlugin

from app.db.manager import Database, StorageError
from app.middleware.auth import AuthMiddleware
from app.middleware.json import RequireJSON, JSONTranslator
from app.routes import build_routes


def application(env, start_response):
    set_logging()
    # Build an object to manage our db connections.
    try:
        env_db_host = os.environ["DB_HOST"]
        env_db_name = os.environ["DB_NAME"]
        env_db_user = os.environ["DB_USER"]
        env_db_pass = os.environ["DB_PASS"]
    except KeyError:
        raise falcon.HTTPInternalServerError(
            description="The server could not reach the database, "
            "please contact your account manager.",
            code=9,
        )

    connection = "postgresql+psycopg2://{user}:{pwd}@{host}/{name}".format(
        user=env_db_user, pwd=env_db_pass, host=env_db_host, name=env_db_name
    )
    db = Database(connection)
    db.setup()

    app = route(db)

    return app(env, start_response)


def route(db):
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
