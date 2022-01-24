
class VarDoctorSignUp:
    # Click on SignUp Button
    SIGNUP_XPATH = '//*[@id="signUp"]'
    
    # SignUp Data
    DOCTOR_NAME_XPATH = '//*[@id="name"]'
    DOCTOR_NAME = "Souvik Ghosh"
    DOCTOR_SPECALITY_XPATH = '//*[@id="specality"]'
    DOCTOR_SPECALITY = "DNA"
    DOCTOR_EMAIL_XPATH = '//*[@id="email"]'
    DOCTOR_EMAIL = "doctor@innovaccer.com"
    DOCTOR_GENDER_XPATH = '//*[@id="gender"]'
    DOCTOR_GENDER = 'Male'
    DOCTOR_PHONE_NUMBER_XPATH = '//*[@id="phone"]'
    DOCTOR_PHONE_NUMBER = '8450042512'
    DOCTOR_PASSWORD_XPATH = '//*[@id="password"]'
    DOCTOR_C_PASSWORD_XPATH = '//*[@id="cpassword"]'
    DOCTOR_PASSWORD = 'A12@asdfgh'
    DOCTOR_C_PASSWORD = 'A12@asdfgh'
    DOCTOR_CLINIC_ADDRESS_XPATH = '//*[@id="clinic_address"]'
    DOCTOR_CLINIC_ADDRESS = 'I have no clinic to provide address. Sorry!!!'
    
    # Submit Click
    SUBMIT_XPATH = '//*[@id="container"]/div[1]/form/button'
    