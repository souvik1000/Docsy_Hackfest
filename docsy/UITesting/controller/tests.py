# from django.test import TestCase
# import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from UITesting.controller.pageobject.locator.checks import Check
from selenium.webdriver.chrome.options import Options
from UITesting.controller.pageobject.pages.doctorsignup import DoctorSignUp
from UITesting.controller.pageobject.pages.patientsignup import PatientSignUp


# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    selenium = webdriver.Chrome('chromedriver')
    
    def test_01_doctor_signup(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Check.BASE_URL)
        DoctorSignUp.check_signup(self, driver)
        self.assertEqual(Check.DOCTOR_SIGNUP_URL, driver.current_url, "Error in SignUp")
        
    def test_02_patient_signup(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Check.BASE_URL)
        PatientSignUp.check_signup(self, driver)
        self.assertEqual(Check.PATIENT_SIGNUP_URL, driver.current_url, "Error in SignUp")

        
        
    
        