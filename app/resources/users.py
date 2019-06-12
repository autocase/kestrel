import logging

import falcon
from falcon.media.validators.jsonschema import validate
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError

from app.db import models
from app.resources import BaseResource
from app.schemas import load_schema

log = logging.getLogger(__name__)


class UserSchema(Schema):
    id = fields.Int(required=False, primary_key=True)
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
        users = models.Users.get_list(self.db.session)

        resp.status = falcon.HTTP_200
        resp.media = {"users": users}

    @validate(load_schema("user_creation"))
    def on_post(self, req, resp):
        """
        ---
        description: Add a new user
        security:
            - BearerAuth: []
        requestBody:
          content:
            application/json:
              schema: UserSchema
        responses:
          200:
            description: New user was saved successfully
            content:
              application/json:
                schema: UserSchema
          400:
            description: User already exists error

        """
        model = models.Users(name=req.media.get("name"))

        try:
            user = model.save(self.db.session)
            resp.status = falcon.HTTP_201
            resp.media = user
        except IntegrityError:
            raise falcon.HTTPBadRequest(
                "Username already exists", "Could not create user due to username already existing"
            )
