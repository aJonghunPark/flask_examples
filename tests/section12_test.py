import pytest
from apps.app import create_app


@pytest.fixture()
def app():
    app = create_app("testing")
    app.config.update({"TESTING": True})

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/section12/")
    assert b"<p>Please login or register!</p>" in response.data
