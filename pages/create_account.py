from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_account_form(self, login, password):

        first_name_field = self.find_element(loc.first_name_field_loc)
        last_name_field = self.find_element(loc.last_name_field_loc)
        email_field = self.find_element(loc.email_field_loc)
        password_field = self.find_element(loc.password_field_loc)
        confirm_password_field = self.find_element(loc.confirm_password_field_loc)
        create_account_button = self.find_element(loc.create_account_button_loc)

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)
        create_account_button.click()



    def check_error_alert_text_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.error_locator))

        error_alert = self.driver.find_element(*loc.error_locator)
        assert error_alert.text == text