from unittest import expectedFailure
from django.test import TestCase
import os.path
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from patient.pageobject.pages.patientlogin import PatientLogin
from patient.pageobject.pages.patienthomepage import PatientHomePage
from patient.pageobject.pages.appointmentpage import AppointmentPage

from patient.pageobject.locator.get import GetPage


# Create your tests here.
class PatientFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
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
        # op = webdriver.ChromeOptions()
        # p = {'download.default_directory': '/home/i1639/jan21/Docsy_Hackfest/docsy/static/image'}
        # op.add_experimental_option('prefs', p)
        # driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=op)
        # driver.maximize_window()
        PatientHomePage.downloadprescription(self,driver)
        # while not os.path.exists('home/i1639/jan21/Docsy_Hackfest/docsy/static/image'):
        #     time.sleep(2)
        
        #     if os.path.isfile('home/i1639/jan21/Docsy_Hackfest/docsy/static/image'):
        #         print("File download is completed")
        #     else:
        #         print("File download is not completed")
        # #close browser
        #     driver.quit()
# # Create your tests here.
# class PlayerFormTest(LiveServerTestCase):
#     selenium = webdriver.Chrome()
    
#     def test_patient(self):
#         driver = self.selenium


#         driver.get('http://127.0.0.1:8000/patient/patientlogin/')

#         #patientlogin
#         time.sleep(1)
#         email=driver.find_element_by_xpath('//*[@id="sign_in_email"]').send_keys('pavan@gmail.com')
#         password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]').send_keys('Pavan@123')
#         login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()


#         # for appointment



#         # driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click
