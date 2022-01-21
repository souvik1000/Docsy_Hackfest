import time
# from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from receptionist.pageobject.pages.appointment import Appointment
from receptionist.pageobject.locators.vardiagnostic import VarDiagnostic

class Daignostic:
    def lab_report_single_data(self, driver):
        driver.find_element_by_xpath(VarDiagnostic.LAB_EVENT_XPATH).send_keys(VarDiagnostic.LAB_EVENT)
        driver.find_element_by_xpath(VarDiagnostic.LAB_TEST_NAME_XPATH).send_keys(VarDiagnostic.LAB_TEST_NAME)
        driver.find_element_by_xpath(VarDiagnostic.LAB_TEST_SPECIMEN_XPATH).send_keys(VarDiagnostic.LAB_TEST_SPECIMEN)
        driver.find_element_by_xpath(VarDiagnostic.LAB_TEST_SPECIMEN_METHOD_XPATH).send_keys(VarDiagnostic.LAB_TEST_SPECIMEN_METHOD)
        driver.find_element_by_xpath(VarDiagnostic.LAB_TEST_SPECIMEN_BODYSITE_XPATH).send_keys(VarDiagnostic.LAB_TEST_SPECIMEN_BODYSITE)
        driver.find_element_by_xpath(VarDiagnostic.LAB_REPORT_XPATH).send_keys(VarDiagnostic.LAB_REPORT)
        driver.find_element_by_xpath(VarDiagnostic.LAB_FILE_INPUT_XPATH).send_keys(VarDiagnostic.LAB_FILE_INPUT)
        
    
    def lab_report_multiple_data(self, driver, lab_counter):
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_EVENT_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_EVENT)
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_TEST_NAME_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_TEST_NAME)
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_TEST_SPECIMEN_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_TEST_SPECIMEN)
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_TEST_SPECIMEN_METHOD_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_TEST_SPECIMEN_METHOD)
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_TEST_SPECIMEN_BODYSITE_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_TEST_SPECIMEN_BODYSITE)
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_REPORT_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_REPORT)
        driver.find_element_by_xpath(VarDiagnostic.LAB_M_FILE_INPUT_XPATH.format(lab_counter+1)).send_keys(VarDiagnostic.LAB_M_FILE_INPUT)
        lab_counter+=1
        
        
    def image_report_single_data(self, driver):
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_EVENT_XPATH).send_keys(VarDiagnostic.IMAGE_EVENT)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_TEST_NAME_XPATH).send_keys(VarDiagnostic.IMAGE_TEST_NAME)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_TEST_MODALITY_XPATH).send_keys(VarDiagnostic.IMAGE_TEST_MODALITY)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_BODY_SITE_XPATH).send_keys(VarDiagnostic.IMAGE_BODY_SITE)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_FINDING_XPATH).send_keys(VarDiagnostic.IMAGE_FINDING)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_FILE_INPUT_XPATH).send_keys(VarDiagnostic.IMAGE_FILE_INPUT)
    
    
    def image_report_multiple_data(self, driver, image_counter):
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_M_EVENT_XPATH.format(image_counter+1)).send_keys(VarDiagnostic.IMAGE_M_EVENT)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_M_TEST_NAME_XPATH.format(image_counter+1)).send_keys(VarDiagnostic.IMAGE_M_TEST_NAME)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_M_TEST_MODALITY_XPATH.format(image_counter+1)).send_keys(VarDiagnostic.IMAGE_M_TEST_MODALITY)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_M_BODY_SITE_XPATH.format(image_counter+1)).send_keys(VarDiagnostic.IMAGE_M_BODY_SITE)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_M_FINDING_XPATH.format(image_counter+1)).send_keys(VarDiagnostic.IMAGE_M_FINDING)
        driver.find_element_by_xpath(VarDiagnostic.IMAGE_M_FILE_INPUT_XPATH.format(image_counter+1)).send_keys(VarDiagnostic.IMAGE_M_FILE_INPUT)
        
        
    def add_button_lab_report(self, driver):
        add_lab = driver.find_element_by_xpath(VarDiagnostic.ADD_LAB_REPORT_BUTTON_XPATH)
        driver.execute_script(VarDiagnostic.ARGUMENT_CLICK, add_lab)
        time.sleep(1)
        
        
    def close_button_lab_report(self, driver):
        close_lab = driver.find_element_by_xpath(VarDiagnostic.CLOSE_LAB_REPORT_BUTTON_XPATH)
        driver.execute_script(VarDiagnostic.ARGUMENT_CLICK, close_lab)
        
        
    def add_button_image_report(self, driver):
        add_image = driver.find_element_by_xpath(VarDiagnostic.ADD_IMAGE_REPORT_BUTTON_XPATH)
        driver.execute_script(VarDiagnostic.ARGUMENT_CLICK, add_image)
        time.sleep(1)
        
        
    def close_button_image_report(self, driver):
        close_image = driver.find_element_by_xpath(VarDiagnostic.CLOSE_IMAGE_REPORT_BUTTON_XPATH)
        driver.execute_script(VarDiagnostic.ARGUMENT_CLICK, close_image)
        time.sleep(1)
        
        
    def submit_data(self, driver):
        submit=driver.find_element_by_xpath(VarDiagnostic.SUBMIT_BUTTON_XPATH)
        driver.execute_script(VarDiagnostic.ARGUMENT_CLICK, submit)
        time.sleep(2)
        
        
    def add_single_lab_report(self, driver):
        Appointment.click_on_add_report(self, driver)
        time.sleep(1)
        Daignostic.add_button_lab_report(self, driver)
        time.sleep(1)
        Daignostic.lab_report_single_data(self, driver)
        time.sleep(1)
        Daignostic.submit_data(self, driver)
        
        
    def add_single_image_report(self, driver):
        Appointment.click_on_add_report(self, driver)
        time.sleep(1)
        Daignostic.add_button_image_report(self, driver)
        time.sleep(1)
        Daignostic.image_report_single_data(self, driver)
        time.sleep(1)
        Daignostic.submit_data(self, driver)
        
        
    def click_close_button_lab_report(self, driver):
        Appointment.click_on_add_report(self, driver)
        time.sleep(1)
        Daignostic.add_button_lab_report(self, driver)
        time.sleep(1)
        Daignostic.close_button_lab_report(self, driver)
        time.sleep(1)
        try:
            driver.find_element_by_xpath(VarDiagnostic.LAB_TEST_NAME_XPATH).send_keys(VarDiagnostic.LAB_TEST_NAME)
        except ElementNotInteractableException:
            return True
        return False
        
        
    def click_close_button_image_report(self, driver):
        Appointment.click_on_add_report(self, driver)
        time.sleep(1)
        Daignostic.add_button_image_report(self, driver)
        time.sleep(1)
        Daignostic.close_button_image_report(self, driver)
        time.sleep(1)
        try:
            driver.find_element_by_xpath(VarDiagnostic.IMAGE_TEST_NAME_XPATH).send_keys(VarDiagnostic.IMAGE_TEST_NAME)
        except ElementNotInteractableException:
            return True
        return False
        
        
        
        