import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

"""
import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensurer_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://addressbook.u0541324.cp.regruhosting.ru/")
"""
