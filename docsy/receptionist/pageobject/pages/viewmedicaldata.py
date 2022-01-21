import time
from receptionist.pageobject.pages.appointment import Appointment
from receptionist.pageobject.locators.varviewmedicaldata import VarViewMedicalData
from receptionist.pageobject.locators.vardiagnostic import VarDiagnostic

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

       
    def check_diagenostic_data(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        # History of Diagnostic View
        driver.find_element_by_xpath(VarViewMedicalData.DIAGNOSTIC_BUTTON_XPATH).click()
        
        
    def check_diagenostic_data_from_home(self, driver):
        Appointment.click_on_medecine_from_home(self, driver)
        time.sleep(1)
        # History of Diagnostic View
        driver.find_element_by_xpath(VarViewMedicalData.DIAGNOSTIC_BUTTON_XPATH).click()
        time.sleep(1)
        
        
    def view_lab_data(self, driver):
        lab_header_names = [VarViewMedicalData.LAB_H_EVENT, VarViewMedicalData.LAB_H_TEST_NAME, VarViewMedicalData.LAB_H_SPECIMEN_TYPE, VarViewMedicalData.LAB_H_SPECIMEN_METHOD, VarViewMedicalData.LAB_H_SPECIMEN_BODY_SITE, VarViewMedicalData.LAB_H_FINDINGS, VarViewMedicalData.LAB_H_DOCUMENT]
        single_lab_details = [VarDiagnostic.LAB_EVENT, VarDiagnostic.LAB_TEST_NAME, VarDiagnostic.LAB_TEST_SPECIMEN, VarDiagnostic.LAB_TEST_SPECIMEN_METHOD, VarDiagnostic.LAB_TEST_SPECIMEN_BODYSITE, VarDiagnostic.LAB_REPORT]
        for i in range(1,8):
            self.assertEqual(driver.find_element_by_xpath(VarViewMedicalData.LAB_HEADER_XPATH.format(i)).text,lab_header_names[i-1], "Lab Header are not matched")
            if i<7:
                self.assertEqual(driver.find_element_by_xpath(VarViewMedicalData.LAB_TABLE_XPATH.format(i)).text,single_lab_details[i-1], "Lab Data are not matched")
        driver.find_element_by_xpath(VarViewMedicalData.LAB_REPORT_VIEW_BUTTON_XPATH).click()
        
        
    def view_image_data(self, driver):
        image_header_names = [VarViewMedicalData.IMAGING_H_EVENT, VarViewMedicalData.IMAGING_H_TEST_NAME, VarViewMedicalData.IMAGING_H_MODALITY, VarViewMedicalData.IMAGING_H_BODY_SITE, VarViewMedicalData.IMAGING_H_FINDINGS, VarViewMedicalData.IMAGING_H_DOCUMENT]
        single_image_details = [VarDiagnostic.IMAGE_EVENT, VarDiagnostic.IMAGE_TEST_NAME, VarDiagnostic.IMAGE_TEST_MODALITY, VarDiagnostic.IMAGE_BODY_SITE, VarDiagnostic.IMAGE_FINDING]
        for i in range(1,7):
            self.assertEqual(driver.find_element_by_xpath(VarViewMedicalData.IMAGE_HEADER_XPATH.format(i)).text,image_header_names[i-1], "Image Header are not matched")
            if (i<6):
                self.assertEqual(driver.find_element_by_xpath(VarViewMedicalData.IMAGE_TABLE_XPATH.format(i)).text,single_image_details[i-1], "Image Data are not matched")
        view_image_report = driver.find_element_by_xpath(VarViewMedicalData.IMAGE_REPORT_VIEW_BUTTON_XPATH)
        view_image_report.location_once_scrolled_into_view
        driver.execute_script(VarViewMedicalData.ARGUMENT_CLICK, view_image_report)    
        
        
    def check_single_lab_report(self, driver):
        ViewMedicalData.check_diagenostic_data(self, driver)
        time.sleep(1)
        lab_report_button = driver.find_element_by_xpath(VarViewMedicalData.LAB_REPORT_BUTTON_XPATH)
        lab_report_button.location_once_scrolled_into_view
        driver.execute_script(VarViewMedicalData.ARGUMENT_CLICK, lab_report_button)
        ViewMedicalData.view_lab_data(self, driver)
        time.sleep(1)
        
        
    def check_single_image_report(self, driver):
        ViewMedicalData.check_diagenostic_data(self, driver)
        time.sleep(1)
        image_report_button = driver.find_element_by_xpath(VarViewMedicalData.IMAGE_REPORT_BUTTON_XPATH)
        image_report_button.location_once_scrolled_into_view
        driver.execute_script(VarViewMedicalData.ARGUMENT_CLICK, image_report_button)
        ViewMedicalData.view_image_data(self, driver)
        time.sleep(1)
        
    
    def doctor_details_in_diagnostic(self, driver):
        doctor_name = driver.find_element_by_xpath(VarViewMedicalData.DOCTOR_NAME_XPATH).text
        doctor = driver.find_element_by_xpath(VarViewMedicalData.DOCTOR_XPATH).text
        self.assertEqual(doctor_name, VarViewMedicalData.DOCTOR_NAME)
        self.assertEqual(doctor, VarViewMedicalData.DOCTOR)
        doctor_email = driver.find_element_by_xpath(VarViewMedicalData.DOCTOR_EMAIL_XPATH).text
        email = driver.find_element_by_xpath(VarViewMedicalData.EMAIL_XPATH).text
        self.assertEqual(doctor_email, VarViewMedicalData.DOCTOR_EMAIL)
        self.assertEqual(email, VarViewMedicalData.EMAIL)
        doctor_phn = driver.find_element_by_xpath(VarViewMedicalData.DOCTOR_PHN_XPATH).text
        phn = driver.find_element_by_xpath(VarViewMedicalData.PHN_XPATH).text
        self.assertEqual(doctor_phn, VarViewMedicalData.DOCTOR_PHN)
        self.assertEqual(phn, VarViewMedicalData.PHN)


    def check_doctor_details(self, driver):
        ViewMedicalData.check_diagenostic_data_from_home(self, driver)
        time.sleep(1)
        ViewMedicalData.doctor_details_in_diagnostic(self, driver)        

            
    def patient_name_check(self, driver):
        Appointment.click_on_view_medicine(self, driver)
        patient_name = driver.find_element_by_xpath(VarViewMedicalData.PATIENT_NAME_XPATH).text
        patient_age = driver.find_element_by_xpath(VarViewMedicalData.PATIENT_AGE_XPATH).text
        return ([patient_name, patient_age])