'''
You need to do a bit of setup to make Python let you load your bin/app.py file for testing. When we get to Exercise 52 you'll change this, but for now create an empty bin/__init__.py file so Python thinks bin/ is a directory.

'''
from nose.tools import *
import re

def assert_response(resp, contains = None, matches = None, headers = None, status = "200"):
    assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)

    if status == "200":
        assert resp.data, "Response data is empty."

    if contains:
        assert contains in resp.data, "Response does not contain %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response does not match %r" % matches

    if headers:
        assert_equal(resp.headers, headers)
