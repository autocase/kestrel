import logging
import falcon

from app.resources import BaseResource
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
        send_email_to("test")

        resp.status = falcon.HTTP_200
        resp.media = {"email": "success"}
