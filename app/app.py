import os
from wsgiref import simple_server

import falcon

from app.db.manager import Database, StorageError
from app.middleware.auth import AuthMiddleware
from app.middleware.json import RequireJSON, JSONTranslator
from app.resources import users, status, not_found, swagger


from apispec import APISpec
from falcon_apispec import FalconPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

from app.resources.users import UserSchema


def application(env, start_response):
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
    users_resource = users.UserResource(db=db)
    status_resource = status.StatusResource()
    swagger_resource = swagger.SwaggerResource(spec=spec)
    app.add_route("/", status_resource)
    app.add_route("/users", users_resource)
    app.add_route("/docs", swagger_resource)

    # If a responder ever raised an instance of StorageError, pass control to
    # the given handler.
    app.add_error_handler(StorageError, StorageError.handle)
    # Return a 404 Not Found for any requests not in the router
    app.add_sink(not_found.handle_404, "")

    spec.components.schema("Score", schema=UserSchema)
    # Register entities and paths
    spec.path(resource=users_resource)
    # spec.path(resource=status_resource)
    return app


# Useful for debugging problems in your API; works with pdb.set_trace().
if __name__ == "__main__":
    httpd = simple_server.make_server("127.0.0.1", 8000, application)
    httpd.serve_forever()
