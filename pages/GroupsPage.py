from selenium.webdriver.common.by import By
from pages.BaseApp import BasePage


class Locators:
    GROUPS_PAGE_HEADER = (By.XPATH, "//h1[text()='Groups']")
    CREATE_GROUP_BUTTON_UPPER = (By.XPATH, "//input[@name='new'][1]")
    GROUP_IN_LIST = (By.CSS_SELECTOR, "span.group")
    GROUP_CHECKBOX_INPUT = (By.CSS_SELECTOR, "input[type='checkbox']")
    DELETE_GROUP_BUTTON_UPPER = (By.CSS_SELECTOR, "//input[@name='delete'][1]")
    EDIT_GROUP_BUTTON_UPPER = (By.CSS_SELECTOR, "//input[@name='edit'][1]")
    FIRST_GROUP_IN_LIST = (By.CSS_SELECTOR, "//span[@class='group'][1]")


class GroupsPage(BasePage):
    # Нажатие на кнопку "Добавить группу
    def press_add_new_group(self):
        self.find_element(Locators.CREATE_GROUP_BUTTON_UPPER).click()

    # Метод возвращающий количество групп
    def count_groups(self):
        return len(self.find_elements(Locators.GROUP_IN_LIST))

    # Метод выбирающий первую группу из списка
    def select_first_group_in_list(self):
        self.find_element(Locators.GROUP_CHECKBOX_INPUT).click()

    # Метод выбирающий группу по порядковому номеру
    def select_group_by_position(self, index):
        self.find_elements(Locators.GROUP_CHECKBOX_INPUT)[index].click()

    # Метод выбирающий группу по указанному id
    def select_group_by_id(self, elem_id):
        self.find_element(By.CSS_SELECTOR("input[value='" + elem_id + "']")).click()

    # Метод нажимающий на кнопку удалить группу
    def press_delete_btn(self):
        self.find_element(Locators.DELETE_GROUP_BUTTON_UPPER).click()

    # Метод нажимающий на кнопку редактирования группы
    def press_edit_group_btn(self):
        self.find_element(Locators.EDIT_GROUP_BUTTON_UPPER).click()

    # Этот метод ещё нужно переделать, он был основан на объекте, тут будет иначе, наверно
    def delete_group(self, group):
        pass
