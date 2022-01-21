import time
from turtle import home


from receptionist.pageobject.locators.varappointment import VarAppointment
from receptionist.pageobject.pages.homepage import HomePage

class Appointment:        
    def click_on_view_medicine(self, driver):
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.VIEW_MEDICINE_XPATH).click()
        time.sleep(1)

    def check_appointment(self,driver):
        HomePage.doctor_homepage_appointment(self,driver)
        time.sleep(2)
        check_appointment_actual=driver.find_element_by_xpath(VarAppointment.CHECK_APPOINTMENT_ACTUAL_XPATH).text
        check_appointment_expected=VarAppointment.CHECK_APPOINTMENT_EXPECTED
        self.assertEquals(check_appointment_expected, check_appointment_actual)

        