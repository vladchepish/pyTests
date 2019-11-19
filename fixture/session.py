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

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("form[name='logout'] a")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_css_selector("form[name='logout'] b").text == "(" + username + ")"

    def ensurer_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("form[name='logout'] a").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()