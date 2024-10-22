from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def get_one_of_products(self, product_index):
        products_list = self.find_all_elements(loc.products_list_loc)
        return products_list[product_index]


    def add_product_to_wish_list(self, selected_product):
        # Поиск кнопки добавления в список желаемого относительно конкретного продукта
        self.driver.execute_script("window.scrollBy(0, 400);")
        add_to_wish_list_button = selected_product.find_element(By.XPATH, './/a[@class="action towishlist" and @title="Add to Wish List" and @role="button"]')
        ActionChains(self.driver).move_to_element(selected_product).move_to_element(add_to_wish_list_button).click().perform()



