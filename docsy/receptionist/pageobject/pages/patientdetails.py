import sys
sys.path.append("/home/souvik/Desktop/New/Docsy_Hackfest/docsy/receptionist")

import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pageobject.pages.homepage import HomePage
from pageobject.locator import Locator

class PatientDetails:
    def navbar_and_click_appointment(self, driver):
        # Goto NAV Bar
        navbar = driver.find_element_by_xpath('//*[@id="navbarLinks"]')
        navbar.location_once_scrolled_into_view
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="navbarLinks"]/ul/li[2]/a').click()
    
    def patient_details(self, driver):
        # Patient Details
        driver.find_element_by_xpath(Locator.PATIENT_NAME_XPATH).send_keys(Locator.PATIENT_NAME)
        driver.find_element_by_xpath(Locator.PATIENT_PHONENO_XPATH).send_keys(Locator.PATIENT_PHONENO)
        time.sleep(1)
        
    def submit(self, driver):
        # Click Submit
        submit = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[10]/div/input')
        submit.location_once_scrolled_into_view
        time.sleep(1)
        submit.click()
        
    def allergies(self, driver):     
        # Goto Allergies Section
        allergies_section = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/h4[1]')
        allergies_section.location_once_scrolled_into_view
        type = Select(driver.find_element_by_xpath('//*[@id="type"]'))
        type.select_by_visible_text('Intolerance')
        criticality = Select(driver.find_element_by_xpath('//*[@id="criticality"]'))
        criticality.select_by_visible_text('Medium')
        driver.find_element_by_xpath('//*[@id="substance"]').send_keys('Dust')
        driver.find_element_by_xpath('//*[@id="comment"]').send_keys('Take medicines two times a day.')
        
        time.sleep(1)
        
    def procedure(self, driver):
        # Goto Procedure Section
        procedure_section = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/h4[2]')
        procedure_section.location_once_scrolled_into_view
        driver.find_element_by_xpath('//*[@id="procedure_name"]').send_keys('Ligament Injury')
        driver.find_element_by_xpath('//*[@id="procedure_body_site"]').send_keys('Left Leg')
        driver.find_element_by_xpath('//*[@id="date_of_procedure"]').send_keys('10-12-2021')
        
        time.sleep(1)
    
    def illness(self, driver):
        # Goto Illness Section
        illness_section = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/h4[3]')
        illness_section.location_once_scrolled_into_view
        driver.find_element_by_xpath('//*[@id="illness_name"]').send_keys("Fever")
        driver.find_element_by_xpath('//*[@id="illness_body_site"]').send_keys("Head")
        severity = Select(driver.find_element_by_xpath('//*[@id="severity"]'))
        severity.select_by_visible_text('High')
        date_onset = driver.find_element_by_xpath('//*[@id="illness_date_onset"]')
        date_onset.send_keys('10-12-2021')
        date_onset.send_keys(Keys.TAB)
        date_onset.send_keys('0245PM')
        date_abatement = driver.find_element_by_xpath('//*[@id="illness_date_abatement"]')
        date_abatement.send_keys('17-12-2021')
        date_abatement.send_keys(Keys.TAB)
        date_abatement.send_keys('0945AM')
        
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
        
        