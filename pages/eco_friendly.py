from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def fill_create_account_form(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find_element(loc.first_name_field_loc)



