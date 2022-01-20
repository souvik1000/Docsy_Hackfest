from django.test import TestCase

from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    def test4_patient_download_report(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/patient/patientlogin/')
        email=driver.find_element_by_xpath('//*[@id="sign_in_email"]')
        email.send_keys('patient@innovaccer.com')
        password2=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password2.send_keys('A12@asdfgh')
        login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        time.sleep(4) 
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,450);') 
        driver.sleep(4)
        clickreports=driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[2]/a').click()

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
