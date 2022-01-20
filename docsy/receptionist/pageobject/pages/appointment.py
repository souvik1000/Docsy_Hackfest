import time
from receptionist.pageobject.locators.varappointment import VarAppointment

class Appointment:        
    def click_on_view_medicine(self, driver):
        time.sleep(1)
        driver.find_element_by_xpath(VarAppointment.VIEW_MEDICINE_XPATH).click()
        time.sleep(1)
        
        