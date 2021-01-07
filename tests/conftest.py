from pytest import fixture
from app.api import app


@fixture
def client():
    return app.test_client()
