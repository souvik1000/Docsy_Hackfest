from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    def test_view_medical_data(self):
            driver = self.selenium
            driver.get('http://127.0.0.1:8000/doctor/')
            driver.maximize_window()
            time.sleep(2)
            mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
            mobile.send_keys('8450042512')
            password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
            password.send_keys('A12@asdfgh')
            submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 900);") 
            time.sleep(2)
            appointment=driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a').click()
            time.sleep(2)
            viewmed=driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[7]/div/a')
            viewmed.click()
            history=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/button')
            time.sleep(2)
            history.click()
            driver.execute_script("window.scrollTo(0, 550);")
            time.sleep(3)

    def testDoctorData(self):
            driver = self.selenium
            driver.get('http://127.0.0.1:8000/doctor/')
            driver.maximize_window()
            time.sleep(2)
            mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
            mobile.send_keys('8450042512')
            password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
            password.send_keys('A12@asdfgh')
            submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 950);") 
            time.sleep(2)
            appointment=driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a').click()
            time.sleep(2)
            viewmed=driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[7]/div/a')
            viewmed.click()
            history=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/button')
            time.sleep(2)
            history.click()
            driver.execute_script("window.scrollTo(0, 500);")
            docname=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/div/div[1]/p[1]').text
            #print(docname)
            self.assertNotEqual (docname, "", "Doctor name not found")
            docemail=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/div/div[1]/p[2]').text
            #print(docemail)
            self.assertNotEqual (docemail, "", "Doctor email not found")
            docphone=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/div/div[1]/p[3]')
            self.assertNotEqual (docphone, "", "Doctor phone number not found")
            
    
    def test_lab_report(self):
            driver = self.selenium
            driver.get('http://127.0.0.1:8000/doctor/')
            driver.maximize_window()
            time.sleep(2)
            mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
            mobile.send_keys('8450042512')
            password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
            password.send_keys('A12@asdfgh')
            submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 950);") 
            time.sleep(2)
            appointment=driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a').click()
            time.sleep(2)
            viewmed=driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[7]/div/a')
            viewmed.click()
            history=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/button')
            time.sleep(2)
            history.click()
            driver.execute_script("window.scrollTo(0, 710);")
            prevreport=driver.find_element_by_xpath('//*[@id="diagnostic-data"]/div/button[1]')
            prevreport.click()
        


        
