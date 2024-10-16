from faker import Faker
import pytest

fake = Faker()

@pytest.mark.smoke
def test_create_valid_account(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_create_account_form(
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        'pa$$w0rd',
        'pa$$w0rd'
    )
    create_account_page.check_current_url()
