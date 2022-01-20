import sys
sys.path.append("/home/souvik/Desktop/New/Docsy_Hackfest/docsy/receptionist")
import time
from pageobject.pages.login import Login

class HomePage:
    def doctor_homepage_patient_details(self, driver):
        Login.doctor_login(self, driver)
        # Doctor HomePage
        patient_details = driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[3]/a')
        patient_details.location_once_scrolled_into_view
        time.sleep(1)
        patient_details.click()
    
        
    # def doctor_homepage_appointment(self, driver):
    
    
    def doctor_logout(self, driver):
        Login.doctor_login(self, driver)
        # Doctor Logout
        driver.find_element_by_xpath('//*[@id="navbarLinks"]/ul/li[4]/a').click()