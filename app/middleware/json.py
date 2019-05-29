import json

import falcon


class RequireJSON:
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                "This API only supports responses encoded as JSON.", href="https://www.json.org/"
            )

        if req.method in ("POST", "PUT"):
            if "application/json" not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    "This API only supports requests encoded as JSON. "
                    "You are missing application/json in the request header",
                    href="https://www.json.org/",
                )


class JSONTranslator:
    def process_request(self, req, resp):
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if req.content_length in (None, 0):
            # Nothing to do
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest("Empty request body", "A valid JSON document is required.")

        try:
            req.context.doc = json.loads(body.decode("utf-8"))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(
                falcon.HTTP_753,
                "Malformed JSON",
                "Could not decode the request body. The "
                "JSON was incorrect or not encoded as "
                "UTF-8.",
            )

    def process_response(self, req, resp, resource, req_succeeded):
        """Post-processing of the response (after routing).

        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
            req_succeeded: True if no exceptions were raised while
                the framework processed and routed the request;
                otherwise False.
        """


def is_json(my_json):
    try:
        json.loads(my_json)
    except Exception:
        return False
    return True
