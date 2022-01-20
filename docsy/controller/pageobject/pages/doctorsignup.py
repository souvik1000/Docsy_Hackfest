import time
from controller.pageobject.pages.landingpage import LandingPage
from controller.pageobject.locator.vardoctorsignup import VarDoctorSignUp
from selenium.webdriver.support.ui import Select

class DoctorSignUp:
    def doctor_signup_click(self, driver):
        LandingPage.register_as_doctor(self, driver)
        driver.find_element_by_xpath(VarDoctorSignUp.SIGNUP_XPATH).click()
        time.sleep(1)
        
        
    def doctor_signup_data(self, driver):
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_NAME_XPATH).send_keys(VarDoctorSignUp.DOCTOR_NAME)
        time.sleep(1)
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_SPECALITY_XPATH).send_keys(VarDoctorSignUp.DOCTOR_SPECALITY)
        time.sleep(1)
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_EMAIL_XPATH).send_keys(VarDoctorSignUp.DOCTOR_EMAIL)
        time.sleep(1)
        gender = Select(driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_GENDER_XPATH))
        gender.select_by_visible_text(VarDoctorSignUp.DOCTOR_GENDER)
        time.sleep(1)
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_PHONE_NUMBER_XPATH).send_keys(VarDoctorSignUp.DOCTOR_PHONE_NUMBER)
        time.sleep(1)
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_PASSWORD_XPATH).send_keys(VarDoctorSignUp.DOCTOR_PASSWORD)
        time.sleep(1)
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_C_PASSWORD_XPATH).send_keys(VarDoctorSignUp.DOCTOR_C_PASSWORD)
        time.sleep(1)
        driver.find_element_by_xpath(VarDoctorSignUp.DOCTOR_CLINIC_ADDRESS_XPATH).send_keys(VarDoctorSignUp.DOCTOR_CLINIC_ADDRESS)
        time.sleep(1)
        
        
    def submit_data(self, driver):
        driver.find_element_by_xpath(VarDoctorSignUp.SUBMIT_XPATH).click()
        time.sleep(1)
        
    
    def check_signup(self, driver):
        DoctorSignUp.doctor_signup_click(self, driver)
        DoctorSignUp.doctor_signup_data(self, driver)
        DoctorSignUp.submit_data(self, driver)
        