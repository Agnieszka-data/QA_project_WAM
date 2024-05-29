import random
import pytest
import allure
from pages.my_account_page import MyAccountPage

@pytest.mark.usefixtures("setup")

class TestLoginAccount:

    @allure.title("Test logowania - błąd")
    def test_login_account_failed(self):
        email1 = str(random.randint(1, 10000)) + "testeroprogramowania1@op.pl"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.login_account(email1, "Szklanka1.")
        msg = "Użytkownik już istnieje"
        assert msg in my_account_page.get_error_message()

    @allure.title("Test logowania - błąd")
    def test_login_account_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.login_account("testeroprogramowania1@op.pl", "Szklanka1.")