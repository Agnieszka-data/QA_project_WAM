import pytest
import allure
import Strings from strings
from pages.my_account_page import MyAccountPage

@pytest.mark.usefixtures("setup")

class TestCreateAccount:

    @allure.title("Test tworzenia konta - błąd")
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("testeroprogramowania1@op.pl", "Szklanka1.", "Szklanka1.")
        my_account_page.button_click()
        assert Strings.msg in my_account_page.get_error_message()

    @allure.title("Test tworzenia konta - poprawny")
    def test_create_account_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("testeroprogramowania123@op.pl", "Szklanka1.", "Szklanka1.")
        my_account_page.button_click()
