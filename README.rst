A Flask web-handler for the Google Appengine deferred library.

::

    from flask import Flask
    import FlaskDeferredHandler

    app = Flask(__name__)
    FlaskDeferredHandler.register(app)


Kinda stupid? Ah well