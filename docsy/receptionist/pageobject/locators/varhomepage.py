from docsy.receptionist.pageobject.pages.appointment import Appointment


class VarHomePage:
    # Below Patient Detatils
    HOME_PATIENT_DETAILS_XPATH = '/html/body/div/section[2]/div/div/div[3]/a'
    
    # NAVBAR Logout 
    HOME_NAVBAR_LOGOUT_XPATH = '//*[@id="navbarLinks"]/ul/li[4]/a'

    # REGISTER PATIENT
    REGISTER_XPATH='/html/body/div/section[1]/div/div/div[2]/div/div/a'
    
    # click appointment button
    APPOINTMENT_XPATH='/html/body/div/section[2]/div/div/div[1]/a'
    