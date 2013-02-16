import sys, os
import pytest

APP_ROOT = os.path.realpath(__file__)
GAESDK_PATH = "c:\dev\gae"

def fix_sys_path(path):
    sys.path.insert(0, path)

    import dev_appserver
    dev_appserver.fix_sys_path()

def pytest_addoption(parser):
    group = parser.getgroup("gae", "google app engine plugin")
    group.addoption('--waterf-sdk', action='store', dest='gaesdk_path',
                    metavar='PATH', default=GAESDK_PATH,
                    help="Google App Engine's root PATH")

def pytest_configure(config):
    fix_sys_path(config.option.gaesdk_path)



@pytest.fixture
def taskqueue(request, bed):
    from google.appengine.ext import testbed
    bed.init_taskqueue_stub(root_path=APP_ROOT)
    return bed.get_stub(testbed.TASKQUEUE_SERVICE_NAME)

@pytest.fixture
def blobstore(request, bed):
    bed.init_blobstore_stub()
    bed.init_files_stub()
    from google.appengine.api import files
    return files

@pytest.fixture
def ndb(bed):
    from google.appengine.datastore import datastore_stub_util
    bed.init_memcache_stub()
    policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=0)
    bed.init_datastore_v3_stub(consistency_policy=policy)

    from google.appengine.ext import ndb
    return ndb

@pytest.fixture
def fastndb(bed):
    from google.appengine.datastore import datastore_stub_util
    bed.init_memcache_stub()
    policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=1)
    bed.init_datastore_v3_stub(consistency_policy=policy)

    from google.appengine.ext import ndb
    return ndb



@pytest.fixture
def bed(request):
    from google.appengine.ext import testbed
    bed = testbed.Testbed()
    bed.activate()
    request.addfinalizer(lambda: bed.deactivate())
    return bed


