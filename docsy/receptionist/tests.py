from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import datetime
from datetime import date
from django.utils import timezone
import pytz
from datetime import datetime

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    def test1_doctor_login(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(4)
        # Find patient
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8450042512')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('A12@asdfgh')
        submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()

    def test2_register_patient_doctor(self):
        driver=self.selenium 
        driver.get('http://127.0.0.1:8000/doctor/home/')
        time.sleep(5)  
        registerPatient=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
        time.sleep(2)
        email=driver.find_element_by_xpath('//*[@id="sign_in_email"]')
        email.send_keys('patient@innovaccer.com')
        password2=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password2.send_keys('A12@asdfgh')
        login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        time.sleep(4)
        book_appointment=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
        driver.maximize_window()
        specilization= Select(driver.find_element_by_xpath('//*[@id="specalization"]'))
        specilization.select_by_value('Ophthalmologist')
        doctor_select= Select(driver.find_element_by_xpath('//*[@id="Doctor"]'))
        doctor_select.select_by_value('5')
        calendar=driver.find_element_by_xpath('//*[@id="dateControl"]')
       
        calendar.send_keys('10-12-2022')
        calendar.send_keys(Keys.TAB)
        calendar.send_keys('0245PM')
        

        
        disease=driver.find_element_by_xpath('//*[@id="disease"]')
        disease.send_keys('serious problem')
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(3)
        submit2=driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[5]/div/input')
        submit2.click()
        
       


    def test3_book_appointment_view(self):
        # driver = self.selenium
        # driver.get('http://127.0.0.1:8000/doctor/')
        # time.sleep(4)
        # # Find patient
        # mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        # mobile.send_keys('8450042512')
        # password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        # password.send_keys('A12@asdfgh')
        # submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        # time.sleep(3)
        # driver.maximize_window()
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(4)
        # Find patient
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8450042512')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('A12@asdfgh')
        submit3=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        
        time.sleep(3)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,390);')
        time.sleep(3)
        click_appointment=driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a').click()
        check_appointment_actual=driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[2]/div').text
        check_appointment_expected='Akanksha Kushwaha'
        self.assertEquals(check_appointment_expected, check_appointment_actual)
         
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
        


        
