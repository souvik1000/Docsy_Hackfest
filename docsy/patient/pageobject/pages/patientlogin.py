import time
from receptionist.pageobject.locators.varappointment import VarAppointment
from patient.pageobject.locator.varpatientlogin import VarPatientLogin

class PatientLogin:
    def loginpatient(self,driver):
        email=driver.find_element_by_xpath(VarPatientLogin.EMAIL_XPATH)
        email.send_keys(VarPatientLogin.EMAIL)
        password=driver.find_element_by_xpath(VarPatientLogin.PASSWORD_XPATH)
        password.send_keys(VarPatientLogin.PASSWORD)
        driver.find_element_by_xpath(VarPatientLogin.SUBMIT_XPATH).click()
        time.sleep(1)