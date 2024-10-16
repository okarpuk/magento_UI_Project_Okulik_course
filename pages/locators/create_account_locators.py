from selenium.webdriver.common.by import By


first_name_field_loc = (By.XPATH, '//input[@id="firstname"]')
last_name_field_loc = (By.XPATH, '//input[@id="lastname"]')
email_field_loc = (By.XPATH, '//input[@id="email_address"]')
password_field_loc = (By.XPATH, '//input[@id="password"]')
confirm_password_field_loc = (By.XPATH, '//input[@id="password-confirmation"]')
create_account_button_loc = (By.XPATH, '//button[@title="Create an Account"]')
