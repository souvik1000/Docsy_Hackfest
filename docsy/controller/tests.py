# from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    def test_doctor_signup(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/')
        
        # Find doctor register button
        driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div[2]/div/div[1]/a').click()
        driver.find_element_by_xpath('//*[@id="signUp"]').click()
        
        driver.find_element_by_xpath('//*[@id="name"]').send_keys("Jeshmi Ghosh")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="specality"]').send_keys("DNA")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("ghosh.jeshmi@gmail.com")
        time.sleep(1)
        gender = Select(driver.find_element_by_xpath('//*[@id="gender"]'))
        gender.select_by_visible_text('Female')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys('1234567890')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('A12@asdfgh')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="cpassword"]').send_keys('A12@asdfgh')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="clinic_address"]').send_keys('I have no clinic to provide address. Sorry!!!')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="container"]/div[1]/form/button').click()
        self.assertEqual('http://127.0.0.1:8000/doctor/', driver.current_url, "Error")
        
    def test_patient_login(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div[2]/div/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="signUp"]').click()
        
        driver.find_element_by_xpath('//*[@id="name"]').send_keys("Jeshmi Ghosh")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="dob"]').send_keys("19/09/1999")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("ghosh.jeshmi@gmail.com")
        time.sleep(1)
        gender = Select(driver.find_element_by_xpath('//*[@id="gender"]'))
        gender.select_by_visible_text('Female')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys('1234567890')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('A12@asdfgh')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="cpassword"]').send_keys('A12@asdfgh')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="container"]/div[1]/form/button').click()
        self.assertEqual('http://127.0.0.1:8000/patient/patientlogin/', driver.current_url, "Error")

        
        
    
        