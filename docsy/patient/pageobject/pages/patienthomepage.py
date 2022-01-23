
import time
from patient.pageobject.locator.get import GetPage
from patient.pageobject.locator.varpatienthomepage import VarPatientHomePage
from patient.pageobject.pages.patientlogin import PatientLogin



class PatientHomePage:
    def buttonclick(self,driver):
        PatientLogin.loginpatient(self,driver)
        driver.find_element_by_xpath(VarPatientHomePage.BOOK_BUTTON).click()
        driver.maximize_window()


    def download_report(self,driver):
        PatientLogin.loginpatient(self,driver)
        time.sleep(4) 
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(4)
        clickreports=driver.find_element_by_xpath(VarPatientHomePage.CLICK_DOWNLOAD_LAB).click()
        time.sleep(5)
        downloadlab=driver.find_element_by_xpath(VarPatientHomePage.BUTTTON_LAB).click()
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,800);') 
        time.sleep(5)
        checkdownloadactual=driver.find_element_by_xpath(VarPatientHomePage.DOWNLOAD_LAB_ACTUAL).click()
        time.sleep(2)
        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")
        download_url=driver.execute_script("""
            var items = document.querySelector('downloads-manager')
                .shadowRoot.getElementById('downloadsList').items;
            if (items.every(e => e.state === "COMPLETE"))
                return items.map(e => e.fileUrl || e.file_url)[0];
            """)
        a=download_url.split('.')
        self.assertIn('Lab-Report',a[0])
        self.assertIn('pdf',a[1])
       


        driver.get(GetPage.PATIENT_HOMEPAGE)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(4)
        clickreports=driver.find_element_by_xpath(VarPatientHomePage.CLICK_DOWNLOAD_IMAGING).click()
        time.sleep(5)
        buttonimaging=driver.find_element_by_xpath(VarPatientHomePage.BUTTON_IMAGING).click()
        driver.execute_script('window.scrollTo(0,400);') 
        time.sleep(5)
        checkdownloadactual2=driver.find_element_by_xpath(VarPatientHomePage.DOWNLOAD_IMAGING_ACTUAL).click()
        time.sleep(3)
        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")
        download_url=driver.execute_script("""
            var items = document.querySelector('downloads-manager')
                .shadowRoot.getElementById('downloadsList').items;
            if (items.every(e => e.state === "COMPLETE"))
                return items.map(e => e.fileUrl || e.file_url)[0];
            """)
        a=download_url.split('.')
        self.assertIn('Lab-Report',a[0])
        self.assertIn('pdf',a[1])


    def viewprescription(self,driver):
        driver.get(GetPage.PATIENT_HOMEPAGE)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(4)
        clickviewprescription=driver.find_element_by_xpath(VarPatientHomePage.PRESCRIPTION_VIEW_XPATH)
        clickviewprescription.location_once_scrolled_into_view
        time.sleep(5)
        clickviewprescription.click()
        prescription1click=driver.find_element_by_xpath(VarPatientHomePage.PRESCRIPTION1_XPATH)
        prescription1click.location_once_scrolled_into_view
        # driver.execute_script('window.scrollTo(0,200);') 
        time.sleep(5)
        prescription1click.click()
   
        MedicineNameActual=driver.find_element_by_xpath(VarPatientHomePage.MEDICINE_NAME_VALUE_XPATH).text
        MedicineNameExpected=VarPatientHomePage.MEDICINE_NAME_EXPECTED
        self.assertEquals(MedicineNameActual,MedicineNameExpected)
        time.sleep(2)
        FormActual=driver.find_element_by_xpath(VarPatientHomePage.FORM_VALUE_XPATH).text
        FormExpected=VarPatientHomePage.FORM_VALUE_EXPECTED
        self.assertEquals(FormActual,FormExpected)
        time.sleep(2)
        StrengthActual=driver.find_element_by_xpath(VarPatientHomePage.STRENGTH_VALUE_XPATH).text
        StrengthExpected=VarPatientHomePage.STRENGTH_VALUE_EXPECTED
        self.assertEquals(StrengthActual,StrengthExpected)
        time.sleep(2)
        StrengthUnitActual=driver.find_element_by_xpath(VarPatientHomePage.STRENGTH_UNIT_VALUE_PATH).text
        StrengthUnitExpected=VarPatientHomePage.STRENGTH_UNIT_VALUE_EXPECTED
        self.assertEquals(StrengthUnitActual,StrengthUnitExpected)
        time.sleep(2)
        DiluentActual=driver.find_element_by_xpath(VarPatientHomePage.DILUENT_VALUE_XPATH).text
        DiluentExpected=VarPatientHomePage.DILUENT_VALUE_EXPECTED
        self.assertEquals(DiluentActual,DiluentExpected)
        time.sleep(2)
        DiluentAmountActual=driver.find_element_by_xpath(VarPatientHomePage.DILUENT_AMOUNT_VALUE_XPATH).text
        DiluentAmountExpected=VarPatientHomePage.DILUENT_AMOUNT_VALUE_EXPECTED
        self.assertEquals(DiluentAmountActual,DiluentAmountExpected)
        time.sleep(2)
        DiluentUnitActual=driver.find_element_by_xpath(VarPatientHomePage.DILUENT_UNIT_VALUE_XPATH).text
        DiluentUnitExpected=VarPatientHomePage.DILUENT_UNIT_VALUE_EXPECTED
        self.assertEquals(DiluentUnitActual,DiluentUnitExpected)
        time.sleep(2)
        DosageDirectionsActual=driver.find_element_by_xpath(VarPatientHomePage.DOSAGE_DIRECTIONS_VALUE_XPATH).text
        DosageDirectionsExpected=VarPatientHomePage.DOSAGE_DIRECTIONS_VALUE_EXPECTED
        self.assertEquals(DosageDirectionsActual,DosageDirectionsExpected)
        time.sleep(2)
        FrequencyActual=driver.find_element_by_xpath(VarPatientHomePage.FORM_VALUE_XPATH).text
        FrequencyExpected=VarPatientHomePage.FORM_VALUE_EXPECTED
        self.assertEquals(FrequencyActual,FrequencyExpected)
        time.sleep(2)
        FrequencyUnitActual=driver.find_element_by_xpath(VarPatientHomePage.FREQUENCY_UNIT_VALUE_XPATH).text
        FrequencyUnitExpected=VarPatientHomePage.FREQUENCY_UNIT_VALUE_EXPECTED
        self.assertEquals(FrequencyUnitActual,FrequencyUnitExpected)
        time.sleep(2)
        IntervalActual=driver.find_element_by_xpath(VarPatientHomePage.INTERVAL_VALUE_XPATH).text
        IntervalExpected=VarPatientHomePage.INTERVAL_VALUE_EXPECTED
        self.assertEquals(IntervalActual,IntervalExpected)
        time.sleep(2)
        IntervalUnitActual=driver.find_element_by_xpath(VarPatientHomePage.INTERVAL_UNIT_VALUE_XPATH).text
        IntervalUnitExpected=VarPatientHomePage.INTERVAL_UNIT_VALUE_EXPECTED
        self.assertEquals(IntervalUnitActual,IntervalUnitExpected)
        time.sleep(2)
        NamedEventActual=driver.find_element_by_xpath(VarPatientHomePage.NAMED_TIME_EVENT_VALUE_XPATH).text
        NamedEventExpected=VarPatientHomePage.NAMED_TIME_EVENT_VALUE_EXPECTED
        self.assertEquals(NamedEventActual,NamedEventExpected)
        time.sleep(2)
        ExactTimingActual=driver.find_element_by_xpath(VarPatientHomePage.EXACT_TIMING_CRITICAL_VALUE_XPATH).text
        ExactTimingExpected=VarPatientHomePage.EXACT_TIMING_CRITICAL_VALUE_EXPECTED
        self.assertEquals(ExactTimingActual,ExactTimingExpected)
        time.sleep(2)


    def downloadprescription(self,driver):
        driver.get(GetPage.PATIENT_HOMEPAGE)
        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,450);') 
        time.sleep(4)
        clickviewprescription=driver.find_element_by_xpath(VarPatientHomePage.PRESCRIPTION_VIEW_XPATH).click()
        time.sleep(5)
        prescription1click=driver.find_element_by_xpath(VarPatientHomePage.PRESCRIPTION1_XPATH).click()
        driver.execute_script('window.scrollTo(0,200);') 
        time.sleep(6)
        DownloadPrescriptionButtton=driver.find_element_by_xpath(VarPatientHomePage.DOWNLOAD_PRESCRIPTION_BUTTON_XPATH).click()
        time.sleep(3)
        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")
        download_url=driver.execute_script("""
            var items = document.querySelector('downloads-manager')
                .shadowRoot.getElementById('downloadsList').items;
            if (items.every(e => e.state === "COMPLETE"))
                return items.map(e => e.fileUrl || e.file_url)[0];
            """)
        a=download_url.split('.')
        self.assertIn('patient_prescription',a[0])
        self.assertIn('pdf',a[1])                                                                                                       
        
        
    def patient_logout(self, driver):
        driver.get(GetPage.GET_PATIENT)
        driver.maximize_window()
        PatientLogin.loginpatient(self,driver)
        time.sleep(1)
        driver.find_element_by_xpath(VarPatientHomePage.LOGOUT_XPATH).click()
        







            
