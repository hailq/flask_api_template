import pytest

from . import AppTestClient
from app import create_app


@pytest.fixture
def app():
    app = create_app('testing')

    yield app


@pytest.fixture
def client(app):
    return AppTestClient(app, app.config['USERNAME'], app.config['PASSWORD'])


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
