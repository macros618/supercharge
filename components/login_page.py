from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .utils import Utils


class LoginPage():

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils()

    def load(self):
        self.driver.get(self.url)
        return self

    @property
    def username(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        username_locator = (By.CSS_SELECTOR, '#user-name')
        username_input = wait.until(EC.visibility_of_element_located(username_locator))

        return username_input
        
    @property
    def password(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        pwd_locator = (By.CSS_SELECTOR, '#password')
        pwd_input = wait.until(EC.visibility_of_element_located(pwd_locator))

        return pwd_input

    @property
    def login_button(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        button_locator = (By.CSS_SELECTOR, '#login-button')
        button = wait.until(EC.visibility_of_element_located(button_locator))

        return button

    @property
    def error_close_button(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        button_locator = (By.CSS_SELECTOR, '.error-message-container button')
        button = wait.until(EC.visibility_of_element_located(button_locator))

        return button

    def get_error(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        error_locator = (By.CSS_SELECTOR, '.error-message-container')
        error_container = wait.until(EC.visibility_of_element_located(error_locator))
        
        if error_container.get_attribute("class") == 'error-message-container error':
            return error_container.text
        else:
            return False
    
    def close_error(self):
        return

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        
        ActionChains(self.driver).move_to_element(self.login_button).click(self.login_button).perform()
        return self