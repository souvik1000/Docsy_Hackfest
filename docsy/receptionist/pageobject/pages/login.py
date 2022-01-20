import sys
sys.path.append("/home/souvik/Desktop/New/Docsy_Hackfest/docsy/receptionist")
import time

class Login:
    def doctor_login(self, driver):
        # Login Doctor
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8450042512')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('A12@asdfgh')
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
        time.sleep(1)