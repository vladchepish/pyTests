from selenium.webdriver.common.by import By
from pages.BaseApp import BasePage


class Locators:
    LOGIN_INPUT = (By.CSS_SELECTOR, "input[name='user']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='pass']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input[value='Login']")


class LoginHelper(BasePage):
    # Атомарный метод - заполнения поля логин
    def type_login(self, value):
        self.find_and_fill_field(value=value, locator=Locators.LOGIN_INPUT)

    # Атомарный метод - заполнения поля пароль
    def type_password(self, value):
        self.find_and_fill_field(value=value, locator=Locators.PASSWORD_INPUT)

    # Атомарный метод - нажатия на кнопку submit
    def press_submit_btn(self):
        self.find_element(locator=Locators.SUBMIT_BTN).click()

    # Метод авторизации
    def login(self, login, password):
        self.type_login(login)
        self.type_password(password)
        self.press_submit_btn()
