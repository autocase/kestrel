import json

import falcon
import pytest
from falcon import HTTPBadRequest

from app.middleware.json import JSONTranslator, RequireJSON, is_json


class stream:
    def read(self):
        return None


class req:
    def __init__(self):
        self.content_length = 1
        self.client_accepts_json = True
        self.method = "POST"
        self.content_type = "application/json"
        self.stream = stream()

    def get_header(self, header):
        return header


def test_json_translator_no_body():
    res = {}
    with pytest.raises(HTTPBadRequest):
        JSONTranslator().process_request(req(), res)


def test_json_translator_no_length():
    res = {}
    tmp_req = req()
    tmp_req.content_length = 0
    result = JSONTranslator().process_request(tmp_req, res)
    assert result is None


def test_json_translator():
    res = {}
    tmp_req = req()
    with pytest.raises(falcon.HTTPBadRequest):
        JSONTranslator().process_request(tmp_req, res)


def test_require_json():
    res = {}
    result = RequireJSON().process_request(req(), res)
    assert result is None


def test_require_json_does_not_accept():
    res = {}
    tmp_req = req()
    tmp_req.client_accepts_json = False
    with pytest.raises(falcon.HTTPNotAcceptable):
        RequireJSON().process_request(tmp_req, res)


def test_require_json_no_content_header():
    res = {}
    tmp_req = req()
    tmp_req.content_type = "application/text"
    with pytest.raises(falcon.HTTPUnsupportedMediaType):
        RequireJSON().process_request(tmp_req, res)


def test_is_json():
    a_json = is_json(json.dumps({'key': 'value'}))
    assert a_json is True


def test_is_not_json():
    not_json = is_json({'key': 'value'})
    assert not_json is False
