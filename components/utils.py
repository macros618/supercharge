from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

class Utils(object):

    driver_path = "d:\Work\selenium-test\drivers\geckodriver\geckodriver.exe"
    resolution_x = 800
    resolution_y = 600
    
    def get_driver(self):
        
        driver_service = Service(executable_path=self.driver_path)
        driver_options = Options()
        driver_options.headless = False
        
        driver = webdriver.Firefox(options=driver_options, service=driver_service)
        #driver.set_window_size(self.resolution_x, self.resolution_y)

        return driver      

    