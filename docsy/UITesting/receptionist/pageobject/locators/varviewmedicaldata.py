class VarViewMedicalData:
    # Check Patient Details
    PATIENT_NAME_XPATH = '/html/body/div/div[1]/p[1]/span'
    PATIENT_AGE_XPATH = '/html/body/div/div[1]/p[2]/span'
    
    # Argument Click
    ARGUMENT_CLICK = "arguments[0].click();"
    
    # Click on History of Allergies
    ALLERGIES_BUTTON_XPATH = '//*[@id="Patient-data"]/button[2]'
    SUBSTANCE_XPATH = '//*[@id="allergies-view"]/tbody/tr[1]/td[3]'
    CRITICALITY_XPATH = '//*[@id="allergies-view"]/tbody/tr[1]/td[2]'
    TYPE_XPATH = '//*[@id="allergies-view"]/tbody/tr[1]/td[1]'
    COMMENT_XPATH = '//*[@id="allergies-view"]/tbody/tr[1]/td[4]'
    
    # Click on History of Procedure
    PROCEDURE_BUTTON_XPATH = '//*[@id="Patient-data"]/button[3]'
    PROCEDURE_NAME_XPATH = '//*[@id="procedure-view"]/tbody/tr[1]/td[1]'
    PROCEDURE_BODYSITE_XPATH = '//*[@id="procedure-view"]/tbody/tr[1]/td[2]'
    DATE_OF_PROCEDURE_XPATH = '//*[@id="procedure-view"]/tbody/tr[1]/td[3]'
    
    # Click on History of Illness
    ILLENSS_BUTTON_XPATH = '//*[@id="Patient-data"]/button[4]'
    ILLNESS_NAME_XPATH = '//*[@id="illness-view"]/tbody/tr[1]/td[1]'
    ILLNESS_BODYSITE_XPATH = '//*[@id="illness-view"]/tbody/tr[1]/td[2]'
    ILLNESS_SEVERITY_XPATH = '//*[@id="illness-view"]/tbody/tr[1]/td[3]'
    ILLNESS_DATE_OF_ONSET_XPATH = '//*[@id="illness-view"]/tbody/tr[1]/td[4]'
    ILLNESS_DATE_OF_ABATEMENT_XPATH = '//*[@id="illness-view"]/tbody/tr[1]/td[5]'
    
    # Click on History of Diagnostic Data
    DIAGNOSTIC_BUTTON_XPATH = '//*[@id="diagnostic-data"]/button'
    LAB_REPORT_BUTTON_XPATH = '/html/body/div/div[2]/div[2]/div/button[1]'
    IMAGE_REPORT_BUTTON_XPATH = '/html/body/div/div[2]/div[2]/div/button[2]'
    
    # Check Doctor Details
    DOCTOR_NAME_XPATH = '/html/body/div/div[2]/div[2]/div/div[1]/p[1]/span[1]'
    DOCTOR_XPATH = '/html/body/div/div[2]/div[2]/div/div[1]/p[1]/span[2]'
    DOCTOR_EMAIL_XPATH = '/html/body/div/div[2]/div[2]/div/div[1]/p[2]/span[1]'
    EMAIL_XPATH = '/html/body/div/div[2]/div[2]/div/div[1]/p[2]/span[2]'
    DOCTOR_PHN_XPATH = '/html/body/div/div[2]/div[2]/div/div[1]/p[3]/span[1]'
    PHN_XPATH = '/html/body/div/div[2]/div[2]/div/div[1]/p[3]/span[2]'
    DOCTOR_NAME = "Doctor Name:"
    DOCTOR = "SOUVIK GHOSH"
    DOCTOR_EMAIL = "Doctor Email-Id:"
    EMAIL = "DOCTOR@SAMPLE.COM"
    DOCTOR_PHN = "Doctor Phone-No:"
    PHN = "8450042512"
    
    # Lab Report Header
    LAB_HEADER_XPATH = '/html/body/div/div[2]/div[2]/div/div[2]/div/table/thead/tr/td[{}]'
    LAB_TABLE_XPATH = '/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[{}]'
    LAB_REPORT_VIEW_BUTTON_XPATH = '/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[7]/div/a'
    LAB_H_EVENT='lab_event'
    LAB_H_TEST_NAME='lab_test_name'
    LAB_H_SPECIMEN_TYPE='lab_specimen_type'
    LAB_H_SPECIMEN_METHOD='lab_specimen_method'
    LAB_H_SPECIMEN_BODY_SITE='lab_specimen_body_site'
    LAB_H_FINDINGS='lab_findings'
    LAB_H_DOCUMENT='lab_document'
    
    # Image Report Header
    IMAGE_HEADER_XPATH = '/html/body/div/div[2]/div[2]/div/div[3]/div/table/thead/tr/td[{}]'
    IMAGE_TABLE_XPATH = '/html/body/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[{}]'
    IMAGE_REPORT_VIEW_BUTTON_XPATH = '/html/body/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[6]/div/a'
    IMAGING_H_EVENT='imaging_event'
    IMAGING_H_TEST_NAME='imaging_test_name'
    IMAGING_H_MODALITY='imaging_modality'
    IMAGING_H_BODY_SITE='imaging_body_site'
    IMAGING_H_FINDINGS='imaging_findings'
    IMAGING_H_DOCUMENT='imaging_document'

    #get medicine data
    PREVIOUS_PRESCRIPTIONS_XPATH = '//*[@id="Patient-data"]/button[1]'
    GET_MEDICINE_NAME_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[1]'
    GET_FORM_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[2]'
    GET_STRENGTH_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[3]'
    GETSTRENGTH_UNIT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[4]'
    GETDILUENT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[5]'
    GETDILUENT_AMOUNT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[6]'
    GETDILUENT_UNIT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[7]'
    GETDOSADE_DIRECTIONS_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[8]'
    GETFREQUENCY_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[9]'
    GETFREQUENCY_UNIT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[10]'
    GETINTERVAL_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[11]'
    GETINTERVAL_UNIT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[12]'
    GETNAMED_TIME_EVENT_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[13]'
    GETEXACT_TIMING_CRITICAL_XPATH = '//*[@id="prescription-view"]/tbody/tr[{}]/td[14]'
