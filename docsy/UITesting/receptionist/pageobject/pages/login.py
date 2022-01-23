import time
from UITesting.receptionist.pageobject.locators.varlogin import VarLogin

class Login:
    def doctor_login(self, driver):
        # Login Doctor
        mobile=driver.find_element_by_xpath(VarLogin.MOBILE_NO_XPATH)
        mobile.send_keys(VarLogin.MOBILE_NO)
        password=driver.find_element_by_xpath(VarLogin.PASSWORD_XPATH)
        password.send_keys(VarLogin.PASSWORD)
        driver.find_element_by_xpath(VarLogin.SUBMIT_XPATH).click()
        time.sleep(1)