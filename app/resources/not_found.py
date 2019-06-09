import logging

import falcon

log = logging.getLogger(__name__)


def handle_404(req, res):
    """
    The catch all for any requests that don't hit our router.
    Allow for 200 resp on root path, but 404's everywhere else.
    Args:
        req: Clients request object
        resp: The object being sent back to the Client

    """
    log.info("404: Invalid route")
    raise falcon.HTTPNotFound()
