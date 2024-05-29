import allure
import pytest
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestOrderAccount:

    @allure.title("Test składania zamówienia")
    def test_search_account(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.login_account("testeroprogramowania1@op.pl", "Szklanka1.")
        my_account_page.search_account("Kaczkowski")
        self.submit_order_account()

    allure.step('Uzupełnienie formularza')
    def submit_order_account(self):
        submit_order_account.fill_phone_field('555666777')
        submit_order_account.fill_name_field('Tester Oprogramowania')
        submit_order_account.fill_address_field('Słoneczna 1')
        submit_order_account.fill_zip_code_field('11-222')
        submit_order_account.fill_place_field('Warszawa')