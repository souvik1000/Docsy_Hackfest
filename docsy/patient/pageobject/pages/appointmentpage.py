from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from patient.pageobject.locator.varappointmentpage import VarAppointmentPage
from patient.pageobject.pages.patienthomepage import PatientHomePage

class AppointmentPage:
    def appointmentform(self,driver):
        PatientHomePage.buttonclick(self,driver)
        specilization= Select(driver.find_element_by_xpath(VarAppointmentPage.SPECIALIZATION_XPATH))
        specilization.select_by_value(VarAppointmentPage.SPECIALIZATION_VALUE)
        doctor_select= Select(driver.find_element_by_xpath(VarAppointmentPage.DOCTOR_XPATH))
        doctor_select.select_by_value(VarAppointmentPage.DOCTOR_VALUE)
        calendar=driver.find_element_by_xpath(VarAppointmentPage.CALENDAR_XPATH)
       
        calendar.send_keys(VarAppointmentPage.CALENDAR_DATE)
        calendar.send_keys(Keys.TAB)
        calendar.send_keys(VarAppointmentPage.CALENDAR_TIME)
        

        
        disease=driver.find_element_by_xpath(VarAppointmentPage.DISEASE_XPATH)
        disease.send_keys(VarAppointmentPage.DOCTOR_VALUE)
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(3)
        submit2=driver.find_element_by_xpath(VarAppointmentPage.SUBMIT_XPATH)
        submit2.click()