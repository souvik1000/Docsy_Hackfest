import time
from UITesting.patient.pageobject.locator.vardoctorlogin import VarDoctorLogin

class DoctorLogin:
    def logindoctor(self,driver):
        driver.find_element_by_xpath(VarDoctorLogin.MOBILE_XPATH).send_keys(VarDoctorLogin.MOBILE)
        driver.find_element_by_xpath(VarDoctorLogin.PASSWORD_XPATH).send_keys(VarDoctorLogin.PASSWORD)

    def submitclick(self,driver):
        driver.find_element_by_xpath(VarDoctorLogin.SUBMIT_XPATH).click()
        time.sleep(2)

    def checklogin(self,driver):
        DoctorLogin.logindoctor(self,driver)
        DoctorLogin.submitclick(self,driver)             