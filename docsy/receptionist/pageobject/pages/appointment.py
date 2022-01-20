import sys
sys.path.append("/home/souvik/Desktop/New/Docsy_Hackfest/docsy/receptionist")

import time

class Appointment:
    def click_on_view_medicine(self, driver):
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[7]/div/a').click()
        time.sleep(1)
        
        