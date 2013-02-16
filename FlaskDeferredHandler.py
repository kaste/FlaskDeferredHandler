"""
:copyright: (c) 2013 by Herrn Kaste <herr.kaste@gmail.com>.
"""

from flask import Blueprint, request, abort
from google.appengine.ext import deferred

import logging

_DEFAULT_URL = "/_ah/queue/deferred"


dh = Blueprint('deferredhandler', __name__)

def register(app):
    app.register_blueprint(dh, url_prefix=_DEFAULT_URL)



@dh.route('', methods=['POST'])
@dh.route('/<path:path>', methods=['POST'])
def run_from_request(path=None):
    if 'X-AppEngine-TaskName' not in request.headers:
        logging.critical('Detected an attempted XSRF attack. The header '
                       '"X-AppEngine-Taskname" was not set.')
        abort(403)

    headers = ["%s:%s" % (k, v) for k, v in request.headers.items()
               if k.lower().startswith("x-appengine-")]
    logging.info(", ".join(headers))

    try:
        deferred.run(request.data)
    except deferred.PermanentTaskFailure:
        logging.exception("Permanent failure attempting to execute task")

    return "Ok", 200
