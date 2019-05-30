import logging

import falcon
from apispec.utils import validate_spec

from app.resources import BaseResource

log = logging.getLogger(__name__)


class SwaggerResource(BaseResource):
    def on_get(self, req, resp):
        if validate_spec(self.spec):
            resp.status = falcon.HTTP_200
            resp.set_header("Access-Control-Allow-Origin", "*")
            resp.set_header("Access-Control-Allow-Methods", "*")
            resp.set_header("Access-Control-Allow-Headers", "*")

            resp.media = self.spec.to_dict()
        else:
            log.error("OpenAPI spec did not pass validation")
            resp.status = falcon.HTTP_500
