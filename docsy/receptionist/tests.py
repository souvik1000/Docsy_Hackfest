from django.test import TestCase
from distutils.core import setup
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    
    def test1_doctor_login(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/doctor/')
        # driver.maximize_window()
        time.sleep(1)
        # Find patient
        
        mobile=driver.find_element_by_xpath('//*[@id="sign_in_mobile"]')
        mobile.send_keys('8450042512')
        password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]')
        password.send_keys('A12@asdfgh')
        submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()

    def test2_add_and_view_prescription(self):
        driver=self.selenium 
        driver.get('http://127.0.0.1:8000/doctor/home/')
        driver.maximize_window()
        
        # driver.execute_script("window.scrollTo(0, 961);")

        #click on appointment in dashboard
        appointment = driver.find_element_by_xpath("/html/body/div/section[2]/div/div/div[1]/a")
        time.sleep(1)
        appointment.location_once_scrolled_into_view
        time.sleep(1)
        appointment.click()


        #add prescription
        add_prescription=driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[5]/div/a')
        time.sleep(1)
        add_prescription.click()

        #fill prescription of problem details
        problem_name=driver.find_element_by_xpath('//*[@id="problem_name"]')
        problem_body_site=driver.find_element_by_xpath('//*[@id="problem_body_site"]')
        severity=driver.find_element_by_xpath('//*[@id="severity"]')

        time.sleep(0.3)
        problem_name.send_keys('problem1')
        time.sleep(0.3)
        problem_body_site.send_keys('bodysite1')
        time.sleep(0.3)
        severity.send_keys('high')
        
        set_medical_data=[]
        medicines_count=2
        for i in range(1,medicines_count+1):
            add_medicine_btn=driver.find_element_by_xpath('//*[@id="main-section"]/div[2]/div/div/button')
            add_medicine_btn.location_once_scrolled_into_view
            driver.execute_script("arguments[0].click();", add_medicine_btn)
            time.sleep(1)
            # add mecine values
            s='//*[@id="medicine_name{}"]'.format(str(i))
            
            
            medicine_name=driver.find_element_by_xpath('//*[@id="medicine_name{}"]'.format(str(i)))
            form=driver.find_element_by_xpath('//*[@id="form{}"]'.format(str(i)))
            strength=driver.find_element_by_xpath('//*[@id="strength{}"]'.format(str(i)))
            strength_unit=driver.find_element_by_xpath('//*[@id="strength_unit{}"]'.format(str(i)))
            diluent=driver.find_element_by_xpath('//*[@id="diluent{}"]'.format(str(i)))
            diluent_amount=driver.find_element_by_xpath('//*[@id="diluent_amount{}"]'.format(str(i)))
            diluent_unit=driver.find_element_by_xpath('//*[@id="diluent_unit{}"]'.format(str(i)))
            dosade_directions=driver.find_element_by_xpath('//*[@id="dosade_directions{}"]'.format(str(i)))
            frequency=driver.find_element_by_xpath('//*[@id="frequency{}"]'.format(str(i)))
            frequency_unit=Select(driver.find_element_by_xpath('//*[@id="frequency_unit{}"]'.format(str(i))))
            interval=driver.find_element_by_xpath('//*[@id="interval{}"]'.format(str(i)))
            interval_unit=Select(driver.find_element_by_xpath('//*[@id="interval_unit{}"]'.format(str(i))))
            named_time_event=driver.find_element_by_xpath('//*[@id="named_time_event{}"]'.format(str(i)))
            exact_timing_critical=driver.find_element_by_xpath('//*[@id="exact_timing_critical{}"]'.format(str(i)))

            time.sleep(0.3)
            medicine_name.send_keys('medicine{}'.format(str(i)))
            time.sleep(0.3)
            form.send_keys('form{}'.format(str(i)))
            time.sleep(0.3)
            strength.send_keys(i)
            time.sleep(0.3)
            strength_unit.send_keys('mg{}'.format(str(i)))

            time.sleep(0.3)
            diluent.send_keys('diluent{}'.format(str(i)))
            time.sleep(0.3)
            diluent_amount.send_keys(i)
            time.sleep(0.3)
            diluent_unit.send_keys('diluentunit{}'.format(str(i)))
            time.sleep(0.3)
            dosade_directions.send_keys('dosage_directions{}'.format(str(i)))
            time.sleep(0.3)
            frequency.send_keys(i)
            time.sleep(0.3)
            frequency_unit.select_by_visible_text('1/h')
            time.sleep(0.3)
            interval.send_keys(i)
            time.sleep(0.3)
            interval_unit.select_by_visible_text('h')
            time.sleep(0.3)
            named_time_event.send_keys('named time event{}'.format(str(i)))
            time.sleep(0.3)
            exact_timing_critical.click()

            set_medical_data.append(
                ['medicine{}'.format(str(i)),'form{}'.format(str(i)),str(i),'mg{}'.format(str(i)),'diluent{}'.format(str(i)),str(i),'diluentunit{}'.format(str(i)),'dosage_directions{}'.format(str(i)),str(i),'2',str(i),'1','named time event{}'.format(str(i)),'True']
            )
            time.sleep(2)
        
        
       
        submit_prescription=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/input[3]')
        submit_prescription.location_once_scrolled_into_view
        driver.execute_script("arguments[0].click();", submit_prescription)


        # view Medical Data
        view_medical_data=driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr/td[7]/div/a')
        time.sleep(1)
        view_medical_data.click()

        previous_prescriptions=driver.find_element_by_xpath('//*[@id="Patient-data"]/button[1]')
        time.sleep(1)
        previous_prescriptions.click()

        # check medical_data
        get_medicine_data=[]
        check_reports_size=2
        for j in range(1,check_reports_size+1):
            get_medicine_name=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[1]'.format(str(j))).text
            get_form=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[2]'.format(str(j))).text
            get_strength=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[3]'.format(str(j))).text
            getstrength_unit=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[4]'.format(str(j))).text
            getdiluent=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[5]'.format(str(j))).text
            getdiluent_amount=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[6]'.format(str(j))).text
            getdiluent_unit=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[7]'.format(str(j))).text
            getdosade_directions=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[8]'.format(str(j))).text
            getfrequency=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[9]'.format(str(j))).text
            getfrequency_unit=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[10]'.format(str(j))).text
            getinterval=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[11]'.format(str(j))).text
            getinterval_unit=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[12]'.format(str(j))).text
            getnamed_time_event=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[13]'.format(str(j))).text
            getexact_timing_critical=driver.find_element_by_xpath('//*[@id="prescription-view"]/tbody/tr[{}]/td[14]'.format(str(j))).text

            get_medicine_data.append([get_medicine_name,get_form,get_strength,getstrength_unit,getdiluent,getdiluent_amount,getdiluent_unit,getdosade_directions,getfrequency,getfrequency_unit,getinterval,getinterval_unit,getnamed_time_event,getexact_timing_critical])

        

        for givenn in range(len(set_medical_data)):
            for check in range(len(set_medical_data[givenn])):
                self.assertEqual(set_medical_data[givenn][check],get_medicine_data[givenn][check])
                
        


        


   





    


    



        
       

    # def test_register_patient_doctor(self):
    #     driver=self.selenium 
    #     driver.get('http://127.0.0.1:8000/doctor/home/')
    #     time.sleep(2)  
    #     registerPatient=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
    #     time.sleep(2)
    #     email=driver.find_element_by_xpath('//*[@id="sign_in_email"]').send_keys('pavan@gmail.com')
    #     password=driver.find_element_by_xpath('//*[@id="sign_in_pass"]').send_keys('Pavan@123')
    #     login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
    #     time.sleep(4)
    #     book_appointment=driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div[2]/div/div/a').click()
         
# Create your tests here.
    # def test_book_appointement_patient_page(self):
    #     driver=self.selenium 
    #     driver.get('http://127.0.0.1:8000/patient/patientlogin/')
    #     driver.maximize_window()
    #     time.sleep(2)
    #     email=driver.find_element_by_xpath('//*[@id="sign_in_email"]').send_keys('pavan@gmail.com')
    #     password=driver.find_element_by_xpath('//*[@id="signin_pass"]').send_keys('Pavan@123')
    #     login_submit=driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/button').click()
    #     driver.maximize_window()