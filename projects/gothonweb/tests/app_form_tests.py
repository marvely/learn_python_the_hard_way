from nose.tools import *
from bin.app_form import app
from tests.tools import assert_response

def test_hello_form_and_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status = "404")

    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    #make sure default values work for the form
    resp = app.request("/hello", method = "POST")
    assert_response(resp, contains = "Nobody")

    #test that we get expected values
    data = {'name':'Zed', 'greet': 'Hola'}
    resp = app.request('/hello', method = "POST", data = data)
    assert_response(resp, contains = "Zed")

# intentionally break it...
# worked...
