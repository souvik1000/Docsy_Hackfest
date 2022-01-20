import time
from selenium.webdriver.support.ui import Select
from controller.pageobject.pages.landingpage import LandingPage
from controller.pageobject.locator.varpatientsignup import VarPatientSignUp

class PatientSignUp:
    def patient_signup_click(self, driver):
        LandingPage.register_as_patient(self, driver)
        driver.find_element_by_xpath(VarPatientSignUp.SIGNUP_XPATH).click()
        time.sleep(1)
        
    
    def patient_signup_data(self, driver):
        driver.find_element_by_xpath(VarPatientSignUp.PATIENT_NAME_XPATH).send_keys(VarPatientSignUp.PATIENT_NAME)
        time.sleep(1)
        driver.find_element_by_xpath(VarPatientSignUp.PATIENT_DOB_XPATH).send_keys(VarPatientSignUp.PATIENT_DOB)
        time.sleep(1)
        driver.find_element_by_xpath(VarPatientSignUp.PATIENT_EMAIL_XPATH).send_keys(VarPatientSignUp.PATIENT_EMAIL)
        time.sleep(1)
        gender = Select(driver.find_element_by_xpath(VarPatientSignUp.PATIENT_GENDER_XPATH))
        gender.select_by_visible_text(VarPatientSignUp.PATIENT_GENDER)
        time.sleep(1)
        driver.find_element_by_xpath(VarPatientSignUp.PATIENT_PHONE_NO_XPATH).send_keys(VarPatientSignUp.PATIENT_PHONE_NO)
        time.sleep(1)
        driver.find_element_by_xpath(VarPatientSignUp.PATIENT_PASSWORD_XPATH).send_keys(VarPatientSignUp.PATIENT_PASSWORD)
        time.sleep(1)
        driver.find_element_by_xpath(VarPatientSignUp.PATIENT_C_PASSWORD_XPATH).send_keys(VarPatientSignUp.PATIENT_C_PASSWORD)
        time.sleep(1)
    
    
    def submit_data(self, driver):
        driver.find_element_by_xpath(VarPatientSignUp.SUBMIT_PATH).click()
        time.sleep(1)
    
    
    def check_signup(self, driver):
        PatientSignUp.patient_signup_click(self, driver)
        PatientSignUp.patient_signup_data(self, driver)
        PatientSignUp.submit_data(self, driver)