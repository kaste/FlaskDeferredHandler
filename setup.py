import os, re
from setuptools import setup, find_packages

def _read_contents(fn):
    here = os.path.dirname( os.path.realpath(__file__) )
    filename = os.path.join(here, fn)
    with open(filename) as file:
        return file.read()

setup(
    name='FlaskDeferredHandler',
    version='0.1',
    description="A Flask handler for the Google Appengine's deferred library",
    long_description=_read_contents('README.rst'),
    author="herr kaste",
    author_email="herr.kaste@gmail.com",
    license="BSD",
    url='http://github.com/kaste/FlaskDeferredHandler',
    py_modules=['FlaskDeferredHandler'],
    install_requires=['flask'],
    tests_require=['pytest'],
    keywords="flask google appengine gae deferred",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
)


