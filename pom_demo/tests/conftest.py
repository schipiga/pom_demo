import pytest

from pom_demo.app import App
from pom_demo.steps import GoogleSteps


@pytest.yield_fixture
def app():
    _app = App('https://www.google.com.ua/')
    yield _app
    _app.quit()


@pytest.fixture
def google_steps(app):
    return GoogleSteps(app)
