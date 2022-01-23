import time
from UITesting.controller.pageobject.locator.varlandingpage import VartLandingPage

class LandingPage:
    def register_as_doctor(self, driver):
        driver.find_element_by_xpath(VartLandingPage.REGISTER_AS_DOCTOR_XPATH).click()
        time.sleep(1)
        
    
    def register_as_patient(self, driver):
        driver.find_element_by_xpath(VartLandingPage.REGISTER_AS_PATIENT_XPATH).click()
        time.sleep(1)