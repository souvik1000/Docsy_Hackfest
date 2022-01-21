import time
from receptionist.pageobject.pages.login import Login
from receptionist.pageobject.locators.varhomepage import VarHomePage
from controller.pageobject.pages.patientsignup import PatientSignUp
class HomePage:
    def doctor_homepage_patient_details(self, driver):
        Login.doctor_login(self, driver)
        # Doctor HomePage
        patient_details = driver.find_element_by_xpath(VarHomePage.HOME_PATIENT_DETAILS_XPATH)
        patient_details.location_once_scrolled_into_view
        time.sleep(1)
        patient_details.click()
    
        
    def doctor_homepage_appointment(self, driver):
        Login.doctor_login(self,driver)
         
        time.sleep(3)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,390);')
        time.sleep(3)
        click_appointment=driver.find_element_by_xpath(VarHomePage.APPOINTMENT_XPATH).click()
    
    
    def doctor_logout(self, driver):
        Login.doctor_login(self, driver)
        # Doctor Logout
        driver.find_element_by_xpath(VarHomePage.HOME_NAVBAR_LOGOUT_XPATH).click()

    def register(self,driver):
        Login.doctor_login(self,driver)
        time.sleep(5)
        driver.find_element_by_xpath(VarHomePage.REGISTER_XPATH).click()
        time.sleep(2)
        PatientSignUp.check_signup(self.driver)
        time.sleep(4)
      
    