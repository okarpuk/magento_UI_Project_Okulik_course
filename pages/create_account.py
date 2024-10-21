from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from pages.locators.create_account_locators import last_name_empty_error_loc, js_injection_error_loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_account_form(self, first_name, last_name, email, password, confirm_password):
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

    def check_current_url(self):
        current_page_url = self.driver.current_url
        assert current_page_url == "https://magento.softwaretestingboard.com/customer/account/", "Invalid URL"

    def check_empty_last_name_error(self):
        last_name_error = self.driver.find_element(*loc.last_name_empty_error_loc)
        assert last_name_error.text == "This is a required field.", "Last name field should be required"

    def check_js_injection_error(self):
        js_injection_error = self.driver.find_element(*loc.js_injection_error_loc)
        assert js_injection_error.text == "First Name is not valid! Last Name is not valid!", "JS injection can't be entered"
