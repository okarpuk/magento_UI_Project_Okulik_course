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


    def check_products_by_40_50_price_range(self):
        self.driver.execute_script("window.scrollBy(0, 2000);")
        price_button = self.find_element(loc.price_button_loc)
        price_range_40_50 = self.find_element(loc.price_range_40_50_loc)
        price_button.click()
        price_range_40_50.click()
        products_list = self.find_all_elements(loc.products_list_loc)
        for product in products_list:
            price_element = product.find_element(By.XPATH, './/span[@class="price"]')
            price_text = price_element.text
            price_float = float(price_text.replace('$', '').strip())
            assert 40.00 <= price_float <= 49.99, f"Price {price_float} not in range"






    # def check_customer_login_page_name(self):
    #     customer_login_page_name = self.driver.find_element(*loc.customer_login_page_name_loc)
    #     assert customer_login_page_name.text == "Customer Login",\
    #         f"The page name - {customer_login_page_name.text} is invalid"