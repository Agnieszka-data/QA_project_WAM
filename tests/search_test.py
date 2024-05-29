import pytest
from pages.my_account_page import MyAccountPage
import allure

@pytest.mark.usefixtures("setup")
class TestSearchAccount:

    @allure.title("Test wyszukiwarki")
    def test_search_account(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.login_account("testeroprogramowania1@op.pl", "Szklanka1.")
        my_account_page.search_account("Kaczkowski")
