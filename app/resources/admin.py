import logging
import requests

import falcon
from falcon.media.validators.jsonschema import validate
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError

from app.db import models
from app.resources import BaseResource
from app.schemas import load_schema

from app.mail import send_email_to

log = logging.getLogger(__name__)


class AdminResource(BaseResource):
    def on_get(self, req, resp):
        """
        ---
        description: Test Email
        responses:
          200:
            description: A list of users
            content:
              application/json:
                schema:
                    type: array
        """
        send_email_to('test')

        resp.status = falcon.HTTP_200
        resp.media = {"email": 'success'}
