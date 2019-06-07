from app.db.database import StorageError
from app.resources import users, status, not_found, swagger


def build_routes(db, app, spec):
    users_resource = users.UserResource(db=db)
    status_resource = status.StatusResource()
    swagger_resource = swagger.SwaggerResource(spec=spec)

    app.add_route("/", status_resource)

    app.add_route("/users", users_resource)
    spec.path(resource=users_resource)

    app.add_route("/api", swagger_resource)

    # If a responder ever raised an instance of StorageError, pass control to
    # the given handler.
    app.add_error_handler(StorageError, StorageError.handle)
    # Return a 404 Not Found for any requests not in the router
    app.add_sink(not_found.handle_404, "")
