class VarViewMedicalData:
    # Check Patient Details
    PATIENT_NAME_XPATH = '/html/body/div/div[1]/p[1]/span'
    PATIENT_AGE_XPATH = '/html/body/div/div[1]/p[2]/span'
    
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