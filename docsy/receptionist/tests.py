from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class CheckAddReports(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    def test_doctor_add_reports(self):
        driver = self.selenium
        driver.set_window_size(1366, 768)
        driver.get('http://127.0.0.1:8000/doctor/')
        time.sleep(2)
        # Find patient
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8450042512')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('A12@asdfgh')
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()

        # time.sleep(1)
        appointment = driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a')
        time.sleep(3)
        appointment.location_once_scrolled_into_view
        time.sleep(1)
        appointment.click()

        add_report = driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[6]/div/a')
        add_report.location_once_scrolled_into_view
        time.sleep(1)
        add_report.click()

        add_lab_counter=0
        add_image_counter=0
        for each_lab_click in range(2):
            add_lab = driver.find_element_by_xpath('//*[@id="features-creation"]/div/div[2]/button[1]')
            driver.execute_script("arguments[0].click();", add_lab)
            # add_lab.location_once_scrolled_into_view
            # add_lab.click()     
            # print(add_lab_counter)
            #lab results
            if add_lab_counter==0:
                lab_event=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[2]/input')
                lab_event.send_keys('demo_event')

                lab_test_name=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[3]/input')
                lab_test_name.send_keys('demo_test_name')

                lab_test_specimen=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[4]/input')
                lab_test_specimen.send_keys('demo_test_specimen')

                lab_specimen_method=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[5]/input')
                lab_specimen_method.send_keys('demo_test_specimen_method')

                lab_specimen_body_site=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[6]/input')
                lab_specimen_body_site.send_keys('demo_test_body_site')

                lab_finding=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[7]/input')
                lab_finding.send_keys('demo_test_findings')

                File_input=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[8]/input')
                File_input.send_keys("/home/i1611/Pictures/logo.png")
                add_lab_counter+=1
            else:
                # print('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[2]/input'.format(add_lab_counter+1))
                lab_event=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[2]/input'.format(add_lab_counter+1))
                lab_event.send_keys('demo_event')

                lab_test_name=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[3]/input'.format(add_lab_counter+1))
                lab_test_name.send_keys('demo_test_name')

                lab_test_specimen=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[4]/input'.format(add_lab_counter+1))
                lab_test_specimen.send_keys('demo_test_specimen')

                lab_specimen_method=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[5]/input'.format(add_lab_counter+1))
                lab_specimen_method.send_keys('demo_test_specimen_method')

                lab_specimen_body_site=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[6]/input'.format(add_lab_counter+1))
                lab_specimen_body_site.send_keys('demo_test_body_site')

                lab_finding=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[7]/input'.format(add_lab_counter+1))
                lab_finding.send_keys('demo_test_findings')

                File_input=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[8]/input'.format(add_lab_counter+1))
                File_input.send_keys("/home/i1611/Pictures/logo.png")
                add_lab_counter+=1
                # print(add_lab_counter)
        add_lab = driver.find_element_by_xpath('//*[@id="features-creation"]/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", add_lab)
        time.sleep(1)
        close_lab = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/p/b'.format(add_lab_counter+1))
        driver.execute_script("arguments[0].click();", close_lab)

        for each_image_click in range(2):
            add_image = driver.find_element_by_xpath('//*[@id="features-creation"]/div/div[2]/button[2]')
            driver.execute_script("arguments[0].click();", add_image)
            # print(add_image_counter)
            if add_image_counter==0:
                # add_image.location_once_scrolled_into_view
                # add_image.click()  

                #image results
                image_event=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/div[2]/input')
                image_event.send_keys('x')

                image_test_name=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/div[3]/input')
                image_test_name.send_keys('demo_image_test_name')

                image_test_modality=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/div[4]/input')
                image_test_modality.send_keys('demo_image_test_modality')

                image_body_site=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[2]/div[1]/input')
                image_body_site.send_keys('demo_image_body_site')

                image_finding=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[2]/div[2]/input')
                image_finding.send_keys('image_demo_image_findings')

                image_file_input=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[2]/div[3]/input')
                image_file_input.send_keys("/home/i1611/Pictures/logo.png")
                add_image_counter+=1
            else:
                image_event=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div/div[2]/input'.format(add_image_counter+1))
                image_event.send_keys('demo_image_demo_event')

                image_test_name=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div/div[3]/input'.format(add_image_counter+1))
                image_test_name.send_keys('demo_image_test_name')

                image_test_modality=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div/div[4]/input'.format(add_image_counter+1))
                image_test_modality.send_keys('demo_image_test_modality')

                image_body_site=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[2]/div[1]/input'.format(add_image_counter+1))
                image_body_site.send_keys('demo_image_body_site')

                image_finding=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[2]/div[2]/input'.format(add_image_counter+1))
                image_finding.send_keys('image_demo_image_findings')

                image_file_input=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[2]/div[3]/input'.format(add_image_counter+1))
                image_file_input.send_keys("/home/i1611/Pictures/logo.png")
                add_image_counter+=1
        add_image = driver.find_element_by_xpath('//*[@id="features-creation"]/div/div[2]/button[2]')
        driver.execute_script("arguments[0].click();", add_image)
        close_image=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[1]/p/b'.format(add_image_counter+1))
        driver.execute_script("arguments[0].click();", close_image)
        submit=driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/input[4]')
        driver.execute_script("arguments[0].click();", submit)
        time.sleep(2)
        is_dashboard = driver.current_url

        # print(is_dashboard)
        self.assertEquals("http://127.0.0.1:8000/doctor/doctorsDashboard/",is_dashboard)