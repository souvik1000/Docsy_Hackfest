from django.test import LiveServerTestCase
from selenium import webdriver
import time
from patient.pageobject.pages.patienthomepage import PatientHomePage
from patient.pageobject.pages.appointmentpage import AppointmentPage
from selenium.webdriver.chrome.options import Options
from patient.pageobject.locator.get import GetPage


# Create your tests here.
class PatientFormTest(LiveServerTestCase):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    selenium = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    
    
    def test1_book_appointment(self):
        driver=self.selenium 
        driver.get(GetPage.GET_PATIENT)
        time.sleep(5)  
        driver.maximize_window()
        time.sleep(3)
        AppointmentPage.appointmentform(self,driver)
       

    def test2_patient_download_report(self):
        driver = self.selenium
        driver.get(GetPage.GET_PATIENT)
        time.sleep(4) 
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(4)
        PatientHomePage.download_report(self,driver)


    def test3_viewprescription(self):
           driver=self.selenium 
           PatientHomePage.viewprescription(self,driver) 
    
    
    def test4_prescriptiondownload(self):
        driver=self.selenium
        PatientHomePage.downloadprescription(self,driver)
        
        
    def test_05_patient_logout(self):
        driver=self.selenium
        PatientHomePage.patient_logout(self, driver)
        
        
        
