from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        self.wd.quit()