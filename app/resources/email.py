import logging
import falcon

from app.resources import BaseResource
from app.mail import send_email_to

log = logging.getLogger(__name__)


class EmailResource(BaseResource):
    def on_get(self, req, resp):
        """
        ---
        description: Send an email to the given address
        parameters:
        - name: email
          in: query
          description: Email you want to send to
          required: true
          schema:
            type: string
        responses:
          200:
            description: Email was successfully sent
            content:
              application/json:
                schema:
                  type: string
        """
        try:
            email = req.params["email"]
            send_email_to(email)
            resp.status = falcon.HTTP_200
            resp.media = {"email": "success"}
        except KeyError:
            raise falcon.HTTPInvalidParam(
                "You are missing an email parameter", "Missing Parameter"
            )
