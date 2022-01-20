import time
from receptionist.pageobject.pages.appointment import Appointment
from receptionist.pageobject.locators.varviewmedicaldata import VarViewMedicalData

class ViewMedicalData:
    def check_allergies_from_appointment(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Allergies View
        driver.find_element_by_xpath(VarViewMedicalData.ALLERGIES_BUTTON_XPATH).click()
        substance = driver.find_element_by_xpath(VarViewMedicalData.SUBSTANCE_XPATH).text
        criticality = driver.find_element_by_xpath(VarViewMedicalData.CRITICALITY_XPATH).text
        type = driver.find_element_by_xpath(VarViewMedicalData.TYPE_XPATH).text
        comment = driver.find_element_by_xpath(VarViewMedicalData.COMMENT_XPATH).text
        driver.find_element_by_xpath(VarViewMedicalData.ALLERGIES_BUTTON_XPATH).click()
        return(substance, criticality, type, comment)
        
        
    def check_procedures_from_appointment(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Procedure View
        driver.find_element_by_xpath(VarViewMedicalData.PROCEDURE_BUTTON_XPATH).click()
        procedure_name = driver.find_element_by_xpath(VarViewMedicalData.PROCEDURE_NAME_XPATH).text
        body_site = driver.find_element_by_xpath(VarViewMedicalData.PROCEDURE_BODYSITE_XPATH).text
        date_of_procedure = driver.find_element_by_xpath(VarViewMedicalData.DATE_OF_PROCEDURE_XPATH).text
        driver.find_element_by_xpath(VarViewMedicalData.PROCEDURE_BUTTON_XPATH).click()
        return([procedure_name,body_site,date_of_procedure])
        
        
    def check_illness_from_appointment(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Illness View
        driver.find_element_by_xpath(VarViewMedicalData.ILLENSS_BUTTON_XPATH).click()
        illness_name = driver.find_element_by_xpath(VarViewMedicalData.ILLNESS_NAME_XPATH).text
        body_site = driver.find_element_by_xpath(VarViewMedicalData.ILLNESS_BODYSITE_XPATH).text
        severity = driver.find_element_by_xpath(VarViewMedicalData.ILLNESS_SEVERITY_XPATH).text
        date_of_onset = driver.find_element_by_xpath(VarViewMedicalData.ILLNESS_DATE_OF_ONSET_XPATH).text
        date_of_abatement = driver.find_element_by_xpath(VarViewMedicalData.ILLNESS_DATE_OF_ABATEMENT_XPATH).text
        driver.find_element_by_xpath(VarViewMedicalData.ILLENSS_BUTTON_XPATH).click()
        return([illness_name,body_site,severity,date_of_onset,date_of_abatement])
        
        
    def patient_name_check(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        patient_name = driver.find_element_by_xpath(VarViewMedicalData.PATIENT_NAME_XPATH).text
        patient_age = driver.find_element_by_xpath(VarViewMedicalData.PATIENT_AGE_XPATH).text
        return ([patient_name, patient_age])