from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
from application import Application

import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.init_group_creation(Group(name="pyTestsGroup", header="header", footer="footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.init_group_creation(Group(name="", header="", footer=""))
    app.logout()