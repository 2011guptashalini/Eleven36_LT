from os import environ

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    test_name = request.node.name
    build = environ.get('BUILD', "Sample PY Build")
    tunnel_id = environ.get('TUNNEL', False)
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    chrome_options = webdriver.ChromeOptions()
    option = {
    "single_test": {
        "browserName": "Chrome",
        "browserVersion": "121.0",
        "LT:Options": {
            "username": "2011guptashalini",
            "accessKey": "BONUD8qsnqog9BHgcRMWkAqwOcTLMadkrMVJFqp4a3xjijd5ou",
            "visual": True,
            "video": True,
            "platformName": "Windows 10",
            "build": "LambdaTest",
            "project": "Eleven36",
            "name": "Smoke Test",
            "w3c": True,
            "plugin": "python-pytest"
        }
  }
}
    chrome_options.set_capability("LT:Options", option)
    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=chrome_options
    )
    yield browser

    def fin():
        # browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
        # "failed").lower()))
        if request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
