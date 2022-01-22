from django.test import LiveServerTestCase
from selenium import webdriver
from receptionist.pageobject.pages.prescription import Prescription
from receptionist.pageobject.pages.appointment import Appointment
from receptionist.pageobject.pages.patientdetails import PatientDetails
from receptionist.pageobject.pages.viewmedicaldata import ViewMedicalData
from receptionist.pageobject.pages.diagnostic import Daignostic
from receptionist.pageobject.pages.homepage import HomePage
from receptionist.pageobject.pages.patientdetails import PatientDetails
from receptionist.pageobject.pages.viewmedicaldata import ViewMedicalData
from receptionist.pageobject.locators.checks import Checks
from receptionist.pageobject.locators.vardiagnostic import VarDiagnostic
from selenium.webdriver.chrome.options import Options
import time

# Create your tests here.
class ReceptionistAppTest(LiveServerTestCase):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    selenium = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    
    def test_01_patient_details_allergies(self):
        driver = self.selenium 
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(1)
        PatientDetails.add_allergies_data(self, driver)
        substance, criticality, type, comment = ViewMedicalData.check_allergies_from_appointment(self, driver)
        self.assertEqual(substance, "Intolerance", "Data Not Matched")
        self.assertEqual(criticality, "Medium", "Data Not Matched")
        self.assertEqual(type, "Dust", "Data Not Matched")
        self.assertEqual(comment, "Take medicines two times a day.", "Data Not Matched")
        
        
    def test_02_patient_details_procedure(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(1)
        PatientDetails.add_procedure_data(self, driver)
        procedure_name, body_site, date_of_procedure = ViewMedicalData.check_procedures_from_appointment(self, driver)
        self.assertEqual(procedure_name, "Ligament Injury", "Data Not Matched")
        self.assertEqual(body_site, 'Left Leg', "Data Not Matched")
        self.assertEqual(date_of_procedure, "Dec. 10, 2021", "Data Not Matched")
        
        
    def test_03_patient_details_illness(self):
        driver = self.selenium        
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(1)
        PatientDetails.add_illness_data(self, driver)
        illness_name, body_site, severity, date_of_onset, date_of_abatement = ViewMedicalData.check_illness_from_appointment(self, driver)
        self.assertEqual(illness_name, "Fever", "Data Not Matched")
        self.assertEqual(body_site, "Head", "Data Not Matched")
        self.assertEqual(severity, "High", "Data Not Matched")
        self.assertEqual(date_of_onset, "Dec. 10, 2021, 2:45 a.m.", "Data Not Matched")
        self.assertEqual(date_of_abatement, "Dec. 17, 2021, 9:45 a.m.", "Data Not Matched")
        
        
    def test_04_show_today(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        load_data = Appointment.check_data_in_the_table_after_click_todays(self, driver)
        self.assertEqual(load_data, Checks.LOAD_DATA, "No Load All Section")

        
    def test_05_show_load_all(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        todays = Appointment.check_data_in_the_table_after_click_load_all(self, driver)
        self.assertEqual(todays, Checks.NAME_TODAY, "No Load All Section")
        
        
    def test_06_add_single_lab_report(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        Daignostic.add_single_lab_report(self, driver)
        # Now Check Data comes or not
        ViewMedicalData.check_single_lab_report(self, driver)
        file_name = VarDiagnostic.LAB_FILE_INPUT.split('/')[-1].split('.')[0]
        self.assertIn(file_name,driver.current_url, "File Name not Found")
        
    
    def test_07_add_single_image_report(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        Daignostic.add_single_image_report(self, driver)
        # Now Check Data comes or not
        ViewMedicalData.check_single_image_report(self, driver)
        file_name = VarDiagnostic.IMAGE_FILE_INPUT.split('/')[-1].split('.')[0]
        self.assertIn(file_name,driver.current_url, "File Name not Found")
        
        
    def test_08_check_doctor_details_in_diagnostic_view(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        ViewMedicalData.check_doctor_details(self, driver)
            
        
    def test_09_click_close_lab_report(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        self.assertEqual(True, Daignostic.click_close_button_lab_report(self, driver), "Lab Cross Button Not Working")
            
        
    def test_10_click_close_image_report(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        self.assertEqual(True, Daignostic.click_close_button_image_report(self, driver), "Image Cross Button Not Working")
        
        
    def test_11_doctor_mark_as_done(self):
        driver = self.selenium 
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        status = Appointment.click_on_status_appointment(self, driver)
        self.assertEqual(status, Checks.MAKE_AS_NOT_DONE, "Make as not done")


    def test_12_doctor_mark_as_not_done(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(2)
        status = Appointment.click_on_status_recent_appointment(self, driver)
        self.assertEqual(status, Checks.MAKE_AS_DONE, "Make as done")
        
        
    def test_13_logout(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(1)
        HomePage.doctor_logout(self, driver)
        self.assertEqual(Checks.BASE_URL, driver.current_url, "Logout Not Working")

    def test_14_prescription_add_check(self):
        driver = self.selenium
        driver.maximize_window()
        driver.get(Checks.BASE_URL)
        time.sleep(1)
        ViewMedicalData.view_prescription_medicines(self, driver, 2)
        for givenn in range(len(Prescription.set_medical_data)):
            for check in range(len(Prescription.set_medical_data[givenn])):
                self.assertEqual(Prescription.set_medical_data[givenn][check],ViewMedicalData.get_medicine_data[givenn][check])
