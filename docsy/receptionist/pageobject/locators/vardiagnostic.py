import os
BASE_DIR = os.getcwd()

class VarDiagnostic:
    # Add Lab Report
    ADD_LAB_REPORT_BUTTON_XPATH = '//*[@id="features-creation"]/div/div[2]/button[1]'
    CLOSE_LAB_REPORT_BUTTON_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/p/b'
    
    # Add Image Report
    ADD_IMAGE_REPORT_BUTTON_XPATH = '//*[@id="features-creation"]/div/div[2]/button[2]'
    CLOSE_IMAGE_REPORT_BUTTON_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[1]/p/b'
    
    # Lab Report - Single
    LAB_EVENT_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[2]/input'
    LAB_EVENT = 'demo_event'
    LAB_TEST_NAME_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[3]/input'
    LAB_TEST_NAME = 'demo_test_name'
    LAB_TEST_SPECIMEN_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[4]/input'
    LAB_TEST_SPECIMEN = 'demo_test_specimen'
    LAB_TEST_SPECIMEN_METHOD_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[5]/input'
    LAB_TEST_SPECIMEN_METHOD = 'demo_test_specimen_method'
    LAB_TEST_SPECIMEN_BODYSITE_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[6]/input'
    LAB_TEST_SPECIMEN_BODYSITE = 'demo_test_specimen_body_site'
    LAB_REPORT_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[7]/input'
    LAB_REPORT = 'demo_test_findings'
    LAB_FILE_INPUT_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div[8]/input'
    LAB_FILE_INPUT = os.path.join(BASE_DIR, 'static/image/3.jpg')
    
    # Lab Report - Multiple
    LAB_M_EVENT_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[2]/input'
    LAB_M_EVENT = 'demo_event'
    LAB_M_TEST_NAME_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[3]/input'
    LAB_M_TEST_NAME = 'demo_test_name'
    LAB_M_TEST_SPECIMEN_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[4]/input'
    LAB_M_TEST_SPECIMEN = 'demo_test_specimen'
    LAB_M_TEST_SPECIMEN_METHOD_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[5]/input'
    LAB_M_TEST_SPECIMEN_METHOD = 'demo_test_specimen_method'
    LAB_M_TEST_SPECIMEN_BODYSITE_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[6]/input'
    LAB_M_TEST_SPECIMEN_BODYSITE = 'demo_test_specimen_body_site'
    LAB_M_REPORT_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[7]/input'
    LAB_M_REPORT = 'demo_test_findings'
    LAB_M_FILE_INPUT_XPATH = '/html/body/div/div[2]/div/div[1]/form/div[1]/div[{}]/div/div/div/div/div[8]/input'
    LAB_M_FILE_INPUT = os.path.join(BASE_DIR, 'static/image/3.jpg')
    
    # Image Report - Single 
    IMAGE_EVENT_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/div[2]/input'
    IMAGE_EVENT='x'
    IMAGE_TEST_NAME_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/div[3]/input'
    IMAGE_TEST_NAME='demo_image_test_name'
    IMAGE_TEST_MODALITY_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/div[4]/input'
    IMAGE_TEST_MODALITY='demo_image_test_modality'
    IMAGE_BODY_SITE_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[2]/div[1]/input'
    IMAGE_BODY_SITE='demo_image_body_site'
    IMAGE_FINDING_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[2]/div[2]/input'
    IMAGE_FINDING='image_demo_image_findings'
    IMAGE_FILE_INPUT_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div/div/div/div/div[2]/div[3]/input'
    IMAGE_FILE_INPUT=os.path.join(BASE_DIR, 'static/image/3.jpg')
    
    # Image Report - MULTIPLE
    IMAGE_M_EVENT_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div/div[2]/input'
    IMAGE_M_EVENT='demo_image_demo_event'
    IMAGE_M_TEST_NAME_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div/div[3]/input'
    IMAGE_M_TEST_NAME='demo_image_test_name'
    IMAGE_M_TEST_MODALITY_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div/div[4]/input'
    IMAGE_M_TEST_MODALITY='demo_image_test_modality'
    IMAGE_M_BODY_SITE_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[2]/div[1]/input'
    IMAGE_M_BODY_SITE='demo_image_body_site'
    IMAGE_M_FINDING_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[2]/div[2]/input'
    IMAGE_M_FINDING='image_demo_image_findings'
    IMAGE_M_FILE_INPUT_XPATH='/html/body/div/div[2]/div/div[1]/form/div[2]/div[{}]/div/div/div/div[2]/div[3]/input'
    IMAGE_M_FILE_INPUT=os.path.join(BASE_DIR, 'static/image/3.jpg')
    
    
    # Argument Click
    ARGUMENT_CLICK = "arguments[0].click();"
    
    
    
    # Submit Button
    SUBMIT_BUTTON_XPATH = '/html/body/div/div[2]/div/div[1]/form/input[4]'
    
    
    
    
    