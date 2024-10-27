from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class Sale(BasePage):
    page_url = '/sale.html'


    def click_on_cart_icon(self):
        cart_icon = self.find_element(loc.cart_icon_loc)
        cart_icon.click()

    def check_empty_cart_message(self, expected_error_text):
        empty_cart_message = self.find_element(loc.empty_cart_message_loc)
        assert empty_cart_message.text == expected_error_text, "Empty cart message incorrect"


    def find_product_by_search(self, product_name):
        search_field = self.find_element(loc.search_field_loc)
        search_field.send_keys(product_name)
        search_button = self.find_element(loc.search_button_loc)
        search_button.click()

    def click_on_mens_bargains_banner(self):
        mens_bargains_banner = self.find_element(loc.mens_bargains_banner_loc)
        mens_bargains_banner.click()
