import pytest
beforeEach = pytest.mark.usefixtures

from flask import Flask
import FlaskDeferredHandler
from google.appengine.ext import deferred

DEFAULT_URL = FlaskDeferredHandler._DEFAULT_URL

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True

    FlaskDeferredHandler.register(app)
    return app


messages = []

@pytest.fixture
def clear_messages():
    while messages:
        messages.pop()


def A(data):
    messages.append(data)

@beforeEach("clear_messages")
class TestFlaskDeferredHandler:
    def testCatchRoot(self, app, taskqueue):

        task = deferred.defer(A, 'A')
        headers = [('X-AppEngine-TaskName', task.name)]
        with app.test_client() as c:
            rv = c.post(DEFAULT_URL, data=task.payload,
                    headers=[('X-AppEngine-TaskName', task.name)],
                    content_type='application/octet-stream')

            assert ['A'] == messages
            assert rv.status_code == 200

    def testCatchAll(self, app, taskqueue):
        task = deferred.defer(A, 'A')

        with app.test_client() as c:
            rv = c.post(DEFAULT_URL + '/foo/bar',
                    data=task.payload,
                    headers=[('X-AppEngine-TaskName', task.name)],
                    content_type='application/octet-stream')

            assert ['A'] == messages
            assert rv.status_code == 200



