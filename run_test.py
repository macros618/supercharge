from datetime import datetime

from components.utils import Utils
from tests.login_test import LoginTest
from tests.list_test import ListTest

utils = Utils()
login_test = LoginTest()
list_test = ListTest()


"""
TEST 1
"""

try:
    driver = utils.get_driver()
    login_test.login_failed_test(driver)

except AssertionError as e:
    print('[Failed] Test Failed: ' + str(e))
    driver.get_full_page_screenshot_as_file('/screenshots/' + str(datetime.timestamp(datetime.now())) + '.png')
    
except Exception as e:
    print('[Error] An error occured during test run: ' + str(e))
    driver.get_full_page_screenshot_as_file('/screenshots/' + str(datetime.timestamp(datetime.now())) + '.png')
    
finally:
    # Teardown
    driver.quit()
    
"""
TEST 2
"""

try:
    driver = utils.get_driver()
    login_test.login_success_test(driver)
except AssertionError as e:
    print('[Failed] Test Failed: ' + str(e))
    driver.get_full_page_screenshot_as_file('/screenshots/' + str(datetime.timestamp(datetime.now())) + '.png')
    
except Exception as e:
    print('[Error] An error occured during test run: ' + str(e))
    driver.get_full_page_screenshot_as_file('/screenshots/' + str(datetime.timestamp(datetime.now())) + '.png')
    
finally:
    # Teardown
    driver.quit()
    

"""
TEST 3
"""

try:
    driver = utils.get_driver()
    list_test.remove_item_test(driver)
except AssertionError as e:
    print('[Failed] Test Failed: ' + str(e))
    driver.get_full_page_screenshot_as_file('d:\Work\selenium-test\screenshots\\' + str(datetime.timestamp(datetime.now())) + '.png')
    
except Exception as e:
    print('[Error] An error occured during test run: ' + str(e))
    driver.get_full_page_screenshot_as_file('d:\Work\selenium-test\screenshots\\' + str(datetime.timestamp(datetime.now())) + '.png')
    
finally:
    # Teardown
    driver.quit()