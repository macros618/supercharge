from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .utils import Utils


class ListPage():

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils()

    def load(self):
        self.driver.get(self.url)
        return self

    @property
    def menu_button(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        locator = (By.CSS_SELECTOR, '#react-burger-menu-btn')
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    @property
    def menu_button_close(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        locator = (By.CSS_SELECTOR, '#react-burger-cross-btn')
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
    
    @property
    def cart_button(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        locator = (By.CSS_SELECTOR, '#shopping_cart_container>a')
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def open_menu(self):
        ActionChains(self.driver).move_to_element(self.menu_button).click(self.menu_button).perform()
        return self
    
    def close_menu(self):
        ActionChains(self.driver).move_to_element(self.menu_button_close).click(self.menu_button_close).perform()
        return self
    
    def open_cart(self):
        ActionChains(self.driver).move_to_element(self.menu_button).click(self.menu_button).perform()
        return self
        
    def get_product_by_name(self, name):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        locator = (By.XPATH, "//*[text()='" + name + "']/../../../..")
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
    
    def get_product_info(self, element):
        info = {
            'name': element.find_element(By.CSS_SELECTOR, '.inventory_item_name').text,
            'description': element.find_element(By.CSS_SELECTOR, '.inventory_item_desc').text,
            'price': float(element.find_element(By.CSS_SELECTOR, '.inventory_item_price').text[1:]),
            'cart_button_id': element.find_element(By.CSS_SELECTOR, 'button').get_attribute('id')
        }
        
        return info
    
    def add_product_by_name(self, name):
        product_element = self.get_product_by_name(name)
        product_info = self.get_product_info(product_element)
        
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        locator = (By.ID, product_info['cart_button_id'])
        add_to_cart_button = wait.until(EC.visibility_of_element_located(locator))
        
        ActionChains(self.driver).move_to_element(add_to_cart_button).click(add_to_cart_button).perform()
        return self
    
    def remove_product_by_name(self, name):
        product_element = self.get_product_by_name(name)
        product_info = self.get_product_info(product_element)
        
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        locator = (By.ID, product_info['cart_button_id'])
        button = wait.until(EC.visibility_of_element_located(locator))
        
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        return self
    
    def get_cart_item_count(self):
        if self.cart_button.text == '':
            return 0
        else:   
            return int(self.cart_button.text)