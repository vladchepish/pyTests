

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://addressbook.u0541324.cp.regruhosting.ru/")

    def login(self, username, password):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("form[name='logout'] a").click()
        if wd.find_element_by_css_selector("form[name='logout'] a").is_displayed():
            wd.find_element_by_css_selector("form[name='logout'] a").click()