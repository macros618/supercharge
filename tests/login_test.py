from components.utils import Utils
from components.login_page import LoginPage
from components.list_page import ListPage

class LoginTest():

    data = {
        'users': {
                'standard': {'username': 'standard_user', 'password': 'secret_sauce'},
                'lockedout': {'username': 'locked_out_user', 'password': 'secret_sauce'},
                'problem': {'username': 'problem_user', 'password': 'secret_sauce'},
                'perf': {'username': 'performance_glitch_user', 'password': 'secret_sauce'},
                
                'invalid': {'username': 'asdfasdf', 'password': 'asdfsdf'},
            },
        'errors': {
            'wrong_userpass': 'Epic sadface: Username and password do not match any user in this service'
        }
    }

    def __init__(self):
        self.utils = Utils()

    def login_failed_test(self, driver):
        page = LoginPage(driver)
        page.load()
        page.login(self.data['users']['invalid']['username'], self.data['users']['invalid']['password'])
        assert page.get_error() == self.data['errors']['wrong_userpass']
        return True
    
    def login_success_test(self, driver):
        page = LoginPage(driver)
        page.load()
        page.login(self.data['users']['standard']['username'], self.data['users']['standard']['password'])

        # find menu button to validate login
        listPage = ListPage(driver)
        listPage.menu_button

        return True
        