import falcon
from falcon.media.validators.jsonschema import validate
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError

from app.db import models
from app.resources import BaseResource
from app.schemas import load_schema


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)


class UserResource(BaseResource):
    def on_get(self, req, resp):
        """
        ---
        description: Retrieve User information
        responses:
          200:
            description: A list of users
            content:
              application/json:
                schema: UserSchema
        """
        model_list = models.Users.get_list(self.db.session)

        users = [model.as_dict for model in model_list]

        resp.status = falcon.HTTP_200
        resp.media = {"users": users}

    @validate(load_schema("user_creation"))
    def on_post(self, req, resp):
        """
        ---
        description: Add a user
        responses:
          200:
            description: New user was saved successfully
            content:
              application/json:
                schema: UserSchema
        """
        model = models.Users(name=req.media.get("name"))

        try:
            model.save(self.db.session)
        except IntegrityError:
            raise falcon.HTTPBadRequest(
                "Username exists", "Could not create user due to username already existing"
            )

        resp.status = falcon.HTTP_201
        resp.media = {"id": model.id}
