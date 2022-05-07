from components.utils import Utils
from tests.login_test import LoginTest
from components.list_page import ListPage

class ListTest():

    data = {
        'products': {
            'backpack': {'name': 'Sauce Labs Backpack'},
            'tshirt': {'name': 'Sauce Labs Bolt T-Shirt'},
            'light': {'name': 'Sauce Labs Bike Light'}
        }
    }

    def __init__(self):
        self.utils = Utils()

    def login(self, driver):
        login = LoginTest()
        login.login_success_test(driver)

    def menu_test(self, driver):
        self.login(driver)
        
        page = ListPage(driver)
        page.open_menu()
        page.close_menu()
        
        return True

    def add_item_test(self, driver):
        self.login(driver)
        
        page = ListPage(driver)
        page.add_product_by_name(self.data['products']['backpack']['name'])
        assert page.get_cart_item_count() == 1
        
    def remove_item_test(self, driver):
        self.add_item_test(driver)
        
        page = ListPage(driver)
        page.remove_product_by_name(self.data['products']['backpack']['name'])
        assert page.get_cart_item_count() != 0