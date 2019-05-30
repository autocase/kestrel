import logging

import falcon

log = logging.getLogger(__name__)


class AuthMiddleware:
    def process_request(self, req, resp):
        if req.method == "POST":
            token = req.get_header("Authorization")
            account_id = req.get_header("Account-ID")

            challenges = ['Token type="Fernet"']

            if token is None:
                description = "Please provide an auth token as part of the request."
                log.error("Missing Authorization header in request")
                raise falcon.HTTPUnauthorized(
                    "Auth token required",
                    description,
                    challenges,
                    href="http://docs.example.com/auth",
                )

            if not self._token_is_valid(token, account_id):
                description = (
                    "The provided auth token is not valid. "
                    "Please request a new token and try again."
                )
                raise falcon.HTTPUnauthorized(
                    "Authentication required",
                    description,
                    challenges,
                    href="http://docs.example.com/auth",
                )

        return True


def _token_is_valid(token, account_id):
    return True
