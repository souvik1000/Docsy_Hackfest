import time
from UITesting.receptionist.pageobject.pages.appointment import Appointment
from UITesting.receptionist.pageobject.locators.varprescription import VarPrescription
from selenium.webdriver.support.ui import Select


class Prescription:
    def add_prescription(self, driver,medicines_count):
        Appointment.click_on_add_prescription(self, driver)
        time.sleep(1)
        Prescription.problem_data(self, driver)
        time.sleep(1)

        Prescription.set_medical_data=[]
        for med_counter in range(1,medicines_count+1):
            Prescription.set_medical_data.append(Prescription.add_medicine(self,driver,med_counter))
        Prescription.Submit_prescription(self,driver)

    
    def problem_data(self, driver):
        problem_name=driver.find_element_by_xpath(VarPrescription.PROBLEM_NAME_XPATH)
        problem_body_site=driver.find_element_by_xpath(VarPrescription.PROBLEM_BODY_SITE_XPATH)
        severity=driver.find_element_by_xpath(VarPrescription.SEVERITY_XPATH)
        time.sleep(0.3)
        problem_name.send_keys(VarPrescription.PROBLEM_NAME)
        time.sleep(0.3)
        problem_body_site.send_keys(VarPrescription.PROBLEM_BODY_SITE)
        time.sleep(0.3)
        severity.send_keys(VarPrescription.SEVERITY)
        

    def add_medicine(self, driver,med_counter):

        add_medicine_btn=driver.find_element_by_xpath(VarPrescription.ADD_MEDICINE_BTN_XPATH)
        add_medicine_btn.location_once_scrolled_into_view
        driver.execute_script(VarPrescription.ARGUMENT_CLICK, add_medicine_btn)
        time.sleep(1)


        medicine_name=driver.find_element_by_xpath(VarPrescription.MEDICINE_NAME_XPATH.format(str(med_counter)))
        form=driver.find_element_by_xpath(VarPrescription.FORM_XPATH.format(str(med_counter)))
        strength=driver.find_element_by_xpath(VarPrescription.STRENGTH_XPATH.format(str(med_counter)))
        strength_unit=driver.find_element_by_xpath(VarPrescription.STRENGTH_UNIT_XPATH.format(str(med_counter)))
        diluent=driver.find_element_by_xpath(VarPrescription.DILUENT_XPATH.format(str(med_counter)))
        diluent_amount=driver.find_element_by_xpath(VarPrescription.DILUENT_AMOUNT_XPATH.format(str(med_counter)))
        diluent_unit=driver.find_element_by_xpath(VarPrescription.DILUENT_UNIT_XPATH.format(str(med_counter)))
        dosade_directions=driver.find_element_by_xpath(VarPrescription.DOSADE_DIRECTIONS_XPATH.format(str(med_counter)))
        frequency=driver.find_element_by_xpath(VarPrescription.FREQUENCY_XPATH.format(str(med_counter)))
        frequency_unit=Select(driver.find_element_by_xpath(VarPrescription.FREQUENCY_UNIT_XPATH.format(str(med_counter))))
        interval=driver.find_element_by_xpath(VarPrescription.INTERVAL_XPATH.format(str(med_counter)))
        interval_unit=Select(driver.find_element_by_xpath(VarPrescription.INTERVAL_UNIT_XPATH.format(str(med_counter))))
        named_time_event=driver.find_element_by_xpath(VarPrescription.NAMED_TIME_EVENT_XPATH.format(str(med_counter)))
        exact_timing_critical=driver.find_element_by_xpath(VarPrescription.EXACT_TIMING_CRITICAL_XPATH.format(str(med_counter))) 

        time.sleep(0.3)
        medicine_name.send_keys(VarPrescription.MEDICINE_NAME.format(str(med_counter)))

        time.sleep(0.3)
        form.send_keys(VarPrescription.FORM.format(str(med_counter)))

        time.sleep(0.3)
        strength.send_keys(VarPrescription.STRENGTH.format(str(med_counter)))
        time.sleep(0.3)
        strength_unit.send_keys(VarPrescription.STRENGTH_UNIT.format(str(med_counter)))

        time.sleep(0.3)
        diluent.send_keys(VarPrescription.DILUENT.format(str(med_counter)))

        time.sleep(0.3)
        diluent_amount.send_keys(VarPrescription.DILUENT_AMOUNT.format(str(med_counter)))
        
        time.sleep(0.3)
        diluent_unit.send_keys(VarPrescription.DILUENT_UNIT.format(str(med_counter)))
        
        time.sleep(0.3)
        dosade_directions.send_keys(VarPrescription.DOSADE_DIRECTIONS.format(str(med_counter)))
        
        time.sleep(0.3)
        frequency.send_keys(VarPrescription.FREQUENCY.format(str(med_counter)))
        
        time.sleep(0.3)
        frequency_unit.select_by_visible_text(VarPrescription.FREQUENCY_UNIT)
        
        time.sleep(0.3)
        interval.send_keys(VarPrescription.INTERVAL.format(str(med_counter)))
        
        time.sleep(0.3)
        interval_unit.select_by_visible_text(VarPrescription.INTERVAL_UNIT)
        
        time.sleep(0.3)
        named_time_event.send_keys(VarPrescription.NAMED_TIME_EVENT.format(str(med_counter)))
        
        time.sleep(0.3)
        exact_timing_critical.click()

        return [VarPrescription.MEDICINE_NAME.format(str(med_counter)),VarPrescription.FORM.format(str(med_counter)),
        VarPrescription.STRENGTH.format(str(med_counter)),VarPrescription.STRENGTH_UNIT.format(str(med_counter)),
        VarPrescription.DILUENT.format(str(med_counter)),VarPrescription.DILUENT_AMOUNT.format(str(med_counter)),
        VarPrescription.DILUENT_UNIT.format(str(med_counter)),VarPrescription.DOSADE_DIRECTIONS.format(str(med_counter)),
        VarPrescription.FREQUENCY.format(str(med_counter)),VarPrescription.FREQUENCY_UNIT,VarPrescription.INTERVAL.format(str(med_counter)),
        VarPrescription.INTERVAL_UNIT,VarPrescription.NAMED_TIME_EVENT.format(str(med_counter))]

    def Submit_prescription(self, driver):
        submit_prescription=driver.find_element_by_xpath(VarPrescription.SUBMIT_PRESCRIPTION)
        submit_prescription.location_once_scrolled_into_view
        driver.execute_script(VarPrescription.ARGUMENT_CLICK, submit_prescription)
