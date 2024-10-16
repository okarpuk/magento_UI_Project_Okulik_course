from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_login_form(self, login, password):


        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        button = self.find(loc.button_loc)
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()

    def check_error_alert_text_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.error_locator))

        error_alert = self.driver.find_element(*loc.error_locator)
        assert error_alert.text == text