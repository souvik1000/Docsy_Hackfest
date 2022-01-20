# from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from controller.pageobject.locator.checks import Check
from controller.pageobject.pages.doctorsignup import DoctorSignUp
from controller.pageobject.pages.patientsignup import PatientSignUp


# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
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

        
        
    
        