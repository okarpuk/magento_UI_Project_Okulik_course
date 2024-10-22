# from conftest import driver
# from pages.eco_friendly import EcoFriendly
from selenium.webdriver.common.by import By


# eco_friendly_page = EcoFriendly(driver())
# selected_product = eco_friendly_page.get_one_of_products(0)


# Add to wish list locators
products_list_loc = (By.XPATH, '//li[@class="item product product-item"]')
add_to_wish_list_button_loc = products_list_loc[0].find_element(By.XPATH, '//a[@class="action towishlist" and @title="Add to Wish List" and @role="button"]')
customer_login_page_name_loc = (By.XPATH, '//h1[@class="page-title"]')
alert_message = (By.XPATH, '//div[@role="alert"]')











