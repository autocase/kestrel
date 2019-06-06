from app.middleware.auth import AuthMiddleware


class req:
    def __init__(self):
        self.method = "POST"

    def get_header(self, header):
        return header


def test_auth():
    res = {}
    result = AuthMiddleware().process_request(req(), res)
    assert result is True
