import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from UITesting.receptionist.pageobject.pages.homepage import HomePage
from UITesting.receptionist.pageobject.locators.varpatientdetails import VarPatientDetails

class PatientDetails:
    def navbar_and_click_appointment(self, driver):
        time.sleep(1)
        # Goto NAV Bar
        navbar = driver.find_element_by_xpath(VarPatientDetails.NAVBAR_XPATH)
        navbar.location_once_scrolled_into_view
        time.sleep(2)
        driver.find_element_by_xpath(VarPatientDetails.NAVBAR_ALL_APPOINTMENT_XPATH).click()
    
    def patient_details(self, driver):
        # Patient Details
        driver.find_element_by_xpath(VarPatientDetails.PATIENT_NAME_XPATH).send_keys(VarPatientDetails.PATIENT_NAME)
        driver.find_element_by_xpath(VarPatientDetails.PATIENT_PHONENO_XPATH).send_keys(VarPatientDetails.PATIENT_PHONENO)
        time.sleep(1)
        
    def submit(self, driver):
        # Click Submit
        submit = driver.find_element_by_xpath(VarPatientDetails.SUBMIT_XPATH)
        submit.location_once_scrolled_into_view
        time.sleep(1)
        submit.click()
        
    def allergies(self, driver):     
        # Goto Allergies Section
        allergies_section = driver.find_element_by_xpath(VarPatientDetails.ALLERGIES_SECTION_XPATH)
        allergies_section.location_once_scrolled_into_view
        type = Select(driver.find_element_by_xpath(VarPatientDetails.ALLERGIES_TYPE_XPATH))
        type.select_by_visible_text(VarPatientDetails.ALLERGIES_TYPE)
        criticality = Select(driver.find_element_by_xpath(VarPatientDetails.ALLERGIES_CRITICALITY_XPATH))
        criticality.select_by_visible_text(VarPatientDetails.ALLERGIES_CRITICALITY)
        driver.find_element_by_xpath(VarPatientDetails.ALLERGIES_SUBSTANCE_XPATH).send_keys(VarPatientDetails.ALLERGIES_SUBSTANCE)
        driver.find_element_by_xpath(VarPatientDetails.ALLERGIES_COMMENT_XPATH).send_keys(VarPatientDetails.ALLERGIES_COMMENT)
        
        time.sleep(1)
        
    def procedure(self, driver):
        # Goto Procedure Section
        procedure_section = driver.find_element_by_xpath(VarPatientDetails.PROCEDURE_SECTION_XPATH)
        procedure_section.location_once_scrolled_into_view
        driver.find_element_by_xpath(VarPatientDetails.PROCEDURE_NAME_XPATH).send_keys(VarPatientDetails.PROCEDURE_NAME)
        driver.find_element_by_xpath(VarPatientDetails.PROCEDURE_BODYSITE_XPATH).send_keys(VarPatientDetails.PROCEDURE_BODYSITE)
        driver.find_element_by_xpath(VarPatientDetails.PROCEDURE_DATE_OF_PROCEDURE_XPATH).send_keys(VarPatientDetails.PROCEDURE_DATE_OF_PROCEDURE)
        
        time.sleep(1)
    
    def illness(self, driver):
        # Goto Illness Section
        illness_section = driver.find_element_by_xpath(VarPatientDetails.ILLNESS_SECTION_XPATH)
        illness_section.location_once_scrolled_into_view
        driver.find_element_by_xpath(VarPatientDetails.ILLNESS_NAME_XPATH).send_keys(VarPatientDetails.ILLNESS_NAME)
        driver.find_element_by_xpath(VarPatientDetails.ILLNESS_BODYSITE_XPATH).send_keys(VarPatientDetails.ILLNESS_BODYSITE)
        severity = Select(driver.find_element_by_xpath(VarPatientDetails.ILLNESS_SEVERITY_XPATH))
        severity.select_by_visible_text(VarPatientDetails.ILLNESS_SEVERITY)
        date_onset = driver.find_element_by_xpath(VarPatientDetails.ILLNESS_DATE_OF_ONSET_XPATH)
        date_onset.send_keys(VarPatientDetails.ILLNESS_DATE_OF_ONSET)
        date_onset.send_keys(Keys.TAB)
        date_onset.send_keys(VarPatientDetails.ILLNESS_TIME_OF_ONSET)
        date_abatement = driver.find_element_by_xpath(VarPatientDetails.ILLNESS_DATE_OF_ABATEMENT_XPATH)
        date_abatement.send_keys(VarPatientDetails.ILLNESS_DATE_OF_ABATEMENT)
        date_abatement.send_keys(Keys.TAB)
        date_abatement.send_keys(VarPatientDetails.ILLNESS_TIME_OF_ABATEMENT)
        
        time.sleep(1)

    def add_allergies_data(self, driver):
        HomePage.doctor_homepage_patient_details(self, driver)
        PatientDetails.patient_details(self, driver)
        PatientDetails.allergies(self, driver)
        PatientDetails.submit(self, driver)
        PatientDetails.navbar_and_click_appointment(self, driver)
        
    def add_procedure_data(self, driver):
        HomePage.doctor_homepage_patient_details(self, driver)
        PatientDetails.patient_details(self, driver)
        time.sleep(1)
        PatientDetails.procedure(self, driver)
        time.sleep(1)
        PatientDetails.submit(self, driver)
        time.sleep(1)
        PatientDetails.navbar_and_click_appointment(self, driver)
        
    def add_illness_data(self, driver):
        HomePage.doctor_homepage_patient_details(self, driver)
        time.sleep(1)
        PatientDetails.patient_details(self, driver)
        time.sleep(1)
        PatientDetails.illness(self, driver)
        time.sleep(1)
        PatientDetails.submit(self, driver)
        time.sleep(1)
        PatientDetails.navbar_and_click_appointment(self, driver)
        
    def add_all_details(self, driver):
        HomePage.doctor_homepage_patient_details(self, driver)
        time.sleep(1)
        PatientDetails.patient_details(self, driver)
        time.sleep(1)
        PatientDetails.allergies(self, driver)
        time.sleep(1)
        PatientDetails.procedure(self, driver)
        time.sleep(1)
        PatientDetails.illness(self, driver)
        time.sleep(1)
        PatientDetails.submit(self, driver)
        time.sleep(1)
        PatientDetails.navbar_and_click_appointment(self, driver)
        
        