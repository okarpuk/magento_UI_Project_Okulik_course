from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.common.action_chains import ActionChains

from pages.locators.eco_friendly_locators import selected_product


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def get_one_of_products(self, product_index):
        products_list = self.find_all_elements(loc.products_list_loc)
        selected_product = products_list[product_index]
        return selected_product

    def add_product_to_wish_list(self, selected_product):
        (ActionChains(self.driver).move_to_element(selected_product).
         move_to_element(loc.add_to_wish_list_button_loc).click(loc.add_to_wish_list_button_loc).perform())

