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

@pytest.mark.smoke
def test_empty_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_create_account_form(
        fake.first_name(),
        ' ',
        fake.email(),
        'pa$$w0rd',
        'pa$$w0rd'
    )
    create_account_page.check_empty_last_name_error()

@pytest.mark.smoke
def test_send_js_script_in_first_and_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_create_account_form(
        '<script>alert("Ваш сайт уязвим к XSS!");</script>',
        '<script>alert("Ваш сайт уязвим к XSS!");</script>',
        fake.email(),
        'pa$$w0rd',
        'pa$$w0rd'
    )
    create_account_page.check_js_injection_error()

