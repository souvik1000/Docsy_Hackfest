import time
# from receptionist.pageobject.pages.appointment import Appointment
from UITesting.receptionist.pageobject.pages.login import Login
from UITesting.receptionist.pageobject.locators.varhomepage import VarHomePage

class HomePage:
    def doctor_homepage_patient_details(self, driver):
        Login.doctor_login(self, driver)
        # Doctor HomePage
        patient_details = driver.find_element_by_xpath(VarHomePage.HOME_PATIENT_DETAILS_XPATH)
        patient_details.location_once_scrolled_into_view
        time.sleep(1)
        patient_details.click()
    
        
    def doctor_homepage_appointment(self, driver):
        Login.doctor_login(self, driver)
        appointment_section = driver.find_element_by_xpath(VarHomePage.HOME_APPOINTMENT_DETAILS_XPATH)
        appointment_section.location_once_scrolled_into_view
        time.sleep(1)
        appointment_section.click()
    
    
    def doctor_logout(self, driver):
        Login.doctor_login(self, driver)
        # Doctor Logout
        driver.find_element_by_xpath(VarHomePage.HOME_NAVBAR_LOGOUT_XPATH).click()