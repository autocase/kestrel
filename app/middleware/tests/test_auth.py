from app.middleware.auth import AuthMiddleware


class req:
    def __init__(self):
        self.method = "POST"

    def get_header(self, header):
        return header


class res:
    def __init__(self):
        self.method = "POST"

    def set_header(self, header, header_val):
        return header


def test_auth():
    result = AuthMiddleware().process_request(req(), res())
    assert result is True
