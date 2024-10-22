import pytest


@pytest.mark.smoke
def test_create_valid_account(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.get_one_of_products(0)
    eco_friendly_page.add_product_to_wish_list(selected_product=eco_friendly_page.get_one_of_products())
