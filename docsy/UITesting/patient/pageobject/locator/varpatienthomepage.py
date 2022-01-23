class VarPatientHomePage:
    BOOK_BUTTON='/html/body/div/section[1]/div/div/div[2]/div/div/a'
    CLICK_DOWNLOAD_LAB='/html/body/div/section[2]/div/div/div[2]/a'
    BUTTTON_LAB='/html/body/div/section[3]/div/div[2]/div[1]/div/div[4]/div/div/div/a'
    CLICK_DOWNLOAD_IMAGING='/html/body/div/section[2]/div/div/div[3]/a'
    DOWNLOAD_LAB_ACTUAL='/html/body/div[2]/section/div/div[2]/div/div/div/div/a'
   
    BUTTON_IMAGING='/html/body/div/section[4]/div/div[2]/div[1]/div/div[4]/div/div/div/a'
    DOWNLOAD_IMAGING_ACTUAL='/html/body/div[2]/section/div/div[2]/div/div/div/div/a'
     
    # Prescription Medicine
    PRESCRIPTION_VIEW_XPATH='/html/body/div/section[2]/div/div/div[1]/a'
    PRESCRIPTION1_XPATH='/html/body/div/nav/div/ul/li/a'
    MEDICINE_NAME_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[1]/span'
    FORM_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[2]/span'
    STRENGTH_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[3]/span'
    STRENGTH_UNIT_VALUE_PATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[4]/span'
    DILUENT_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[5]/span'
    DILUENT_AMOUNT_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[6]/span'
    DILUENT_UNIT_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[1]/div/ul/li[7]/span'
    DOSAGE_DIRECTIONS_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[1]/span'
    FREQUENCY_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[2]/span'
    FREQUENCY_UNIT_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[3]/span'
    INTERVAL_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[4]/span'
    INTERVAL_UNIT_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[5]/span'
    NAMED_TIME_EVENT_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[6]/span'
    EXACT_TIMING_CRITICAL_VALUE_XPATH='/html/body/div/div[2]/div/div/div/div[2]/div/ul/li[7]/span' 
    DOWNLOAD_PRESCRIPTION_BUTTON_XPATH='/html/body/div/div[2]/div/div/h2/button'
    
    # Medicine Data
    MEDICINE_NAME_EXPECTED='medicine{}'
    FORM_VALUE_EXPECTED='form{}'
    STRENGTH_VALUE_EXPECTED='{}'
    STRENGTH_UNIT_VALUE_EXPECTED='mg{}'
    DILUENT_VALUE_EXPECTED='diluent{}'
    DILUENT_AMOUNT_VALUE_EXPECTED='{}'
    DILUENT_UNIT_VALUE_EXPECTED='diluentunit{}'
    DOSAGE_DIRECTIONS_VALUE_EXPECTED='dosage_directions{}'
    FREQUENCY_VALUE_EXPECTED='{}'
    FREQUENCY_UNIT_VALUE_EXPECTED='1/h'
    INTERVAL_VALUE_EXPECTED='{}'
    INTERVAL_UNIT_VALUE_EXPECTED='h'
    NAMED_TIME_EVENT_VALUE_EXPECTED='named time event{}'
    EXACT_TIMING_CRITICAL_VALUE_EXPECTED='True'
    
    
    # Logout XPath
    LOGOUT_XPATH = '//*[@id="navbarLinks"]/ul/li[6]/a'