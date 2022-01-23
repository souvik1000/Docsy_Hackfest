import time
from UITesting.receptionist.pageobject.locators.varappointment import VarAppointment
from UITesting.receptionist.pageobject.pages.homepage import HomePage

class Appointment:  
    def click_on_todays_from_home(self, driver):
        HomePage.doctor_homepage_appointment(self, driver)
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.TODAY_CHECKBOX_XPATH).click()
        time.sleep(1)
        
          
    def click_on_view_medicine(self, driver):
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.VIEW_MEDICINE_XPATH).click()
        time.sleep(1)
        
        
    def click_on_add_report(self, driver):
        HomePage.doctor_homepage_appointment(self, driver)
        add_report = driver.find_element_by_xpath(VarAppointment.ADD_REPORT_XPATH)
        add_report.location_once_scrolled_into_view
        time.sleep(1)
        add_report.click()
        
        
    def check_data_in_the_table_after_click_todays(self, driver):
        Appointment.click_on_todays_from_home(self, driver)
        return driver.find_element_by_xpath(VarAppointment.LOAD_DATA_XPATH).text
    
    
    def check_data_in_the_table_after_click_load_all(self, driver):
        Appointment.click_on_todays_from_home(self, driver)
        driver.find_element_by_xpath(VarAppointment.LOAD_DATA_XPATH).click()
        return driver.find_element_by_xpath(VarAppointment.TODAY_NAME_XPATH).text
        
        
    def click_on_status_appointment(self, driver):
        HomePage.doctor_homepage_appointment(self, driver)
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.MARK_AS_DONE_XPATH).click()
        return driver.find_element_by_xpath(VarAppointment.MARK_AS_NOT_DONE_XPATH).text
    
    
    def click_on_status_recent_appointment(self, driver):
        HomePage.doctor_homepage_appointment(self, driver)
        time.sleep(1)
        mark_as_not_done = driver.find_element_by_xpath(VarAppointment.MARK_AS_NOT_DONE_XPATH)
        mark_as_not_done.location_once_scrolled_into_view
        time.sleep(1)
        mark_as_not_done.click()
        mark_as_done = driver.find_element_by_xpath(VarAppointment.MARK_AS_DONE_XPATH)
        mark_as_done.location_once_scrolled_into_view
        time.sleep(1)
        return mark_as_done.text
        

    def click_on_medecine_from_home(self, driver):
        HomePage.doctor_homepage_appointment(self, driver)
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.VIEW_MEDICINE_XPATH).click()
        time.sleep(1)

    
    def click_on_add_prescription(self, driver):
        HomePage.doctor_homepage_appointment(self, driver)
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.ADD_PRESCRIPTION_XPATH).click()
        time.sleep(1)

    