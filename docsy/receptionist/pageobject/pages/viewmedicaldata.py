import sys
from tokenize import Comment
sys.path.append("/home/souvik/Desktop/New/Docsy_Hackfest/docsy/receptionist")
import time
from pageobject.pages.appointment import Appointment

class ViewMedicalData:
    name=""
    age=""
    def check_allergies_from_appointment(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Allergies View
        driver.find_element_by_xpath('//*[@id="Patient-data"]/button[2]').click()
        # allergy type
        time.sleep(1)
        substance = driver.find_element_by_xpath('//*[@id="allergies-view"]/tbody/tr[1]/td[3]').text
        criticality = driver.find_element_by_xpath('//*[@id="allergies-view"]/tbody/tr[1]/td[2]').text
        type = driver.find_element_by_xpath('//*[@id="allergies-view"]/tbody/tr[1]/td[1]').text
        comment = driver.find_element_by_xpath('//*[@id="allergies-view"]/tbody/tr[1]/td[4]').text
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="Patient-data"]/button[2]').click()
        return(substance, criticality, type, comment)
        
        
    def check_procedures_from_appointment(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Procedure View
        driver.find_element_by_xpath('//*[@id="Patient-data"]/button[3]').click()
        # procedure type
        procedure_name = driver.find_element_by_xpath('//*[@id="procedure-view"]/tbody/tr[1]/td[1]').text
        body_site = driver.find_element_by_xpath('//*[@id="procedure-view"]/tbody/tr[1]/td[2]').text
        date_of_procedure = driver.find_element_by_xpath('//*[@id="procedure-view"]/tbody/tr[1]/td[3]').text
        # print(procedure_name,body_site,date_of_procedure)
        driver.find_element_by_xpath('//*[@id="Patient-data"]/button[3]').click()
        return([procedure_name,body_site,date_of_procedure])
        
        
    def check_illness_from_appointment(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Illness View
        driver.find_element_by_xpath('//*[@id="Patient-data"]/button[4]').click()
        # illness type
        illness_name = driver.find_element_by_xpath('//*[@id="illness-view"]/tbody/tr[1]/td[1]').text
        body_site = driver.find_element_by_xpath('//*[@id="illness-view"]/tbody/tr[1]/td[2]').text
        severity = driver.find_element_by_xpath('//*[@id="illness-view"]/tbody/tr[1]/td[3]').text
        date_of_onset = driver.find_element_by_xpath('//*[@id="illness-view"]/tbody/tr[1]/td[4]').text
        date_of_abatement = driver.find_element_by_xpath('//*[@id="illness-view"]/tbody/tr[1]/td[5]').text
        # print(illness_name,body_site,severity,date_of_onset,date_of_abatement)
        driver.find_element_by_xpath('//*[@id="Patient-data"]/button[4]').click()
        return([illness_name,body_site,severity,date_of_onset,date_of_abatement])
        
        
    def patient_name_check(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        self.name = driver.find_element_by_xpath('//*[@id="main-section"]/div[1]/p[1]').text
        self.age = driver.find_element_by_xpath('//*[@id="main-section"]/div[1]/p[2]').text