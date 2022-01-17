from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    def test_doctor_login(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(2)
        # Find patient
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8784768489')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('Kirti@1')
        submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()

    def test_register_patient_doctor(self):
        driver=self.selenium 
        driver.get('http://127.0.0.1:8000/doctor/home/')
        time.sleep(2)  
        registerPatient=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
        time.sleep(2)
        email=driver.find_element_by_xpath('//*[@id="sign_in_email"]').send_keys('pavan@gmail.com')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]').send_keys('Pavan@123')
        login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        time.sleep(4)
        book_appointment=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
         
# Create your tests here.
    # def test_book_appointement_patient_page(self):
    #     driver=self.selenium 
    #     driver.get('http://127.0.0.1:8000/patient/patientlogin/')
    #     driver.maximize_window()
    #     time.sleep(2)
    #     email=driver.find_element_by_xpath('//*[@id="sign_in_email"]').send_keys('pavan@gmail.com')
    #     password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]').send_keys('Pavan@123')
    #     login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
    #     driver.maximize_window()
        


        
