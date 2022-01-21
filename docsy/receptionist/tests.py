# import imp
# import sys
# sys.path.append("/home/souvik/Desktop/New/Docsy_Hackfest/docsy/receptionist")
# from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from docsy.patient.pageobject.pages.patientlogin import PatientLogin
from receptionist.pageobject.pages.patientdetails import PatientDetails
from receptionist.pageobject.pages.viewmedicaldata import ViewMedicalData
from receptionist.pageobject.pages.appointment import Appointment

from receptionist.pageobject.pages.homepage import HomePage
from receptionist.pageobject.pages.patientdetails import PatientDetails
# from pageobject.pages.appointment import Appointment
from receptionist.pageobject.pages.viewmedicaldata import ViewMedicalData
from controller.pageobject.locator.checks import Check
from receptionist.pageobject.pages.homepage import HomePage
import time
from patient.pageobject.locator.get import GetPage

# Create your tests here.
class ReceptionistAppTest(LiveServerTestCase):
    selenium = webdriver.Chrome()

    def test1_register_patient_doctor(self):
        driver=self.selenium 
        driver.get(Check.DOCTOR_SIGNUP_URL)
        time.sleep(5)  
        HomePage.register
    
    def test2_book_appointment_view(self):
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
        driver.get(GetPage.GET_PATIENT)
        time.sleep(4)
        # Find patient
        PatientLogin.loginpatient(self,driver)
        time.sleep(3)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,390);')
        time.sleep(3)
        Appointment.check_appointment(self,driver)

    def test3_patient_details_allergies(self):
        driver = self.selenium 
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(1)
        PatientDetails.add_allergies_data(self, driver)
        substance, criticality, type, comment = ViewMedicalData.check_allergies_from_appointment(self, driver)
        self.assertEqual(substance, "Intolerance", "Data Not Matched")
        self.assertEqual(criticality, "Medium", "Data Not Matched")
        self.assertEqual(type, "Dust", "Data Not Matched")
        self.assertEqual(comment, "Take medicines two times a day.", "Data Not Matched")
        
        
    def test4_patient_details_procedure(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(1)
        PatientDetails.add_procedure_data(self, driver)
        procedure_name, body_site, date_of_procedure = ViewMedicalData.check_procedures_from_appointment(self, driver)
        self.assertEqual(procedure_name, "Ligament Injury", "Data Not Matched")
        self.assertEqual(body_site, 'Left Leg', "Data Not Matched")
        self.assertEqual(date_of_procedure, "Dec. 10, 2021", "Data Not Matched")
        
        
    def test5_patient_details_illness(self):
        driver = self.selenium        
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(1)
        PatientDetails.add_illness_data(self, driver)
        illness_name, body_site, severity, date_of_onset, date_of_abatement = ViewMedicalData.check_illness_from_appointment(self, driver)
        self.assertEqual(illness_name, "Fever", "Data Not Matched")
        self.assertEqual(body_site, "Head", "Data Not Matched")
        self.assertEqual(severity, "High", "Data Not Matched")
        self.assertEqual(date_of_onset, "Dec. 10, 2021, 2:45 a.m.", "Data Not Matched")
        self.assertEqual(date_of_abatement, "Dec. 17, 2021, 9:45 a.m.", "Data Not Matched")
        

    def test6_logout(self):
        driver = self.selenium
        driver.maximize_window()
        base_link = 'http://127.0.0.1:8000/doctor/'
        driver.get(base_link)
        time.sleep(1)
        HomePage.doctor_logout(self, driver)
        self.assertEqual(base_link, driver.current_url, "Logout Not Working")