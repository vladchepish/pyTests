from pages.LoginPage import LoginHelper


def test_login(browser):
    login_p = LoginHelper(browser)
    login_p.go_to_site()
    login_p.login(login="admin", password="secret")

