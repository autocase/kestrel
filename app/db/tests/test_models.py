from unittest.mock import patch

import pytest

from app.db.models import Users


@pytest.fixture()
def users():
    return Users('test')


def test_models(users):
    name = users.as_dict
    assert name == {'Name': 'test'}


@patch("app.db.models.session_scope")
def test_save_model(session, users):
    users.save(session)
    assert session.call_count == 1
