import pytest
from time import sleep


@pytest.mark.smoke
def test_add_product_to_wish_list_without_login(eco_friendly_page, customer_login_page):
    eco_friendly_page.open_page()
    selected_product = eco_friendly_page.get_one_of_products(0)
    eco_friendly_page.add_product_to_wish_list(selected_product)
    customer_login_page.check_customer_login_page_name()
    customer_login_page.check_must_login_alert_text()

    sleep(5)


