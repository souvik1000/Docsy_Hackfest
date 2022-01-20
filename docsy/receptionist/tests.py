from django.test import LiveServerTestCase
from selenium import webdriver
from receptionist.pageobject.pages.appointment import Appointment
from receptionist.pageobject.pages.patientdetails import PatientDetails
from receptionist.pageobject.pages.viewmedicaldata import ViewMedicalData

from receptionist.pageobject.pages.homepage import HomePage
from receptionist.pageobject.pages.patientdetails import PatientDetails
from receptionist.pageobject.pages.viewmedicaldata import ViewMedicalData
from receptionist.pageobject.locators.checks import Checks
import time

# Create your tests here.
class ReceptionistAppTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    # def test_01_patient_details_allergies(self):
    #     driver = self.selenium 
    #     driver.maximize_window()
    #     driver.get('http://127.0.0.1:8000/doctor/')
    #     time.sleep(1)
    #     PatientDetails.add_allergies_data(self, driver)
    #     substance, criticality, type, comment = ViewMedicalData.check_allergies_from_appointment(self, driver)
    #     self.assertEqual(substance, "Intolerance", "Data Not Matched")
    #     self.assertEqual(criticality, "Medium", "Data Not Matched")
    #     self.assertEqual(type, "Dust", "Data Not Matched")
    #     self.assertEqual(comment, "Take medicines two times a day.", "Data Not Matched")
        
        
    # def test_02_patient_details_procedure(self):
    #     driver = self.selenium
    #     driver.maximize_window()
    #     driver.get('http://127.0.0.1:8000/doctor/')
    #     time.sleep(1)
    #     PatientDetails.add_procedure_data(self, driver)
    #     procedure_name, body_site, date_of_procedure = ViewMedicalData.check_procedures_from_appointment(self, driver)
    #     self.assertEqual(procedure_name, "Ligament Injury", "Data Not Matched")
    #     self.assertEqual(body_site, 'Left Leg', "Data Not Matched")
    #     self.assertEqual(date_of_procedure, "Dec. 10, 2021", "Data Not Matched")
        
        
    # def test_03_patient_details_illness(self):
    #     driver = self.selenium        
    #     driver.maximize_window()
    #     driver.get('http://127.0.0.1:8000/doctor/')
    #     time.sleep(1)
    #     PatientDetails.add_illness_data(self, driver)
    #     illness_name, body_site, severity, date_of_onset, date_of_abatement = ViewMedicalData.check_illness_from_appointment(self, driver)
    #     self.assertEqual(illness_name, "Fever", "Data Not Matched")
    #     self.assertEqual(body_site, "Head", "Data Not Matched")
    #     self.assertEqual(severity, "High", "Data Not Matched")
    #     self.assertEqual(date_of_onset, "Dec. 10, 2021, 2:45 a.m.", "Data Not Matched")
    #     self.assertEqual(date_of_abatement, "Dec. 17, 2021, 9:45 a.m.", "Data Not Matched")
        

    # def test_04_logout(self):
    #     driver = self.selenium
    #     driver.maximize_window()
    #     base_link = 'http://127.0.0.1:8000/doctor/'
    #     driver.get(base_link)
    #     time.sleep(1)
    #     HomePage.doctor_logout(self, driver)
    #     self.assertEqual(base_link, driver.current_url, "Logout Not Working")
        
        
    # def test_05_show_today(self):
    #     driver = self.selenium
    #     driver.maximize_window()
    #     driver.get(Checks.BASE_URL)
    #     load_data = Appointment.check_data_in_the_table_after_click_todays(self, driver)
    #     self.assertEqual(load_data, Checks.LOAD_DATA, "No Load All Section")

        
    # def test_06_show_load_all(self):
    #     driver = self.selenium
    #     driver.maximize_window()
    #     driver.get(Checks.BASE_URL)
    #     todays = Appointment.check_data_in_the_table_after_click_load_all(self, driver)
    #     self.assertEqual(todays, Checks.NAME_TODAY, "No Load All Section")
        
        
    def test_07_doctor_mark_as_done(self):
        driver = self.selenium 
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        status = Appointment.click_on_status_appointment(self, driver)
        self.assertEqual(status, Checks.MAKE_AS_NOT_DONE, "Make as not done")


    def test_08_doctor_mark_as_not_done(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        status = Appointment.click_on_status_recent_appointment(self, driver)
        self.assertEqual(status, Checks.MAKE_AS_DONE, "Make as done")
        
        
        