from hashlib import new
from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    # def test_doctor_login(self):
    #     driver = self.selenium
    #     driver.get('http://127.0.0.1:8000/doctor/')
    #     time.sleep(2)
    #     # Find patient
    #     mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
    #     mobile.send_keys('8784768489')
    #     password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
    #     password.send_keys('Kirti@1')
    #     submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()

    # def test_register_patient_doctor(self):
    #     driver=self.selenium 
    #     driver.get('http://127.0.0.1:8000/doctor/home/')
    #     time.sleep(2)  
    #     registerPatient=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
    #     time.sleep(2)
    #     email=driver.find_element_by_xpath('//*[@id="sign_in_email"]').send_keys('pavan@gmail.com')
    #     password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]').send_keys('Pavan@123')
    #     login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
    #     time.sleep(4)
    #     book_appointment=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
        
    def test_All_patient_doctor_mark_as_done(self):
        driver=self.selenium 
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(2)   
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8450042512')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('A12@asdfgh')
        submit3=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        time.sleep(2)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,390);')
        time.sleep(2)

        click_appointment=driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/table/tbody/tr/td[8]/div/a').click()
        time.sleep(2)
        Text = driver.find_element_by_xpath('//*[@id="example2"]/tbody/tr/td[5]/div/a').text
        self.assertEquals("Mark as Not done",Text)

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
        


        
