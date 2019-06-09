import logging
import os

import falcon

log = logging.getLogger(__name__)


class StatusResource:
    def on_get(self, req, resp):
        load = os.getloadavg()

        resp.status = falcon.HTTP_200
        resp.media = {"status": "Running", "load": load}
