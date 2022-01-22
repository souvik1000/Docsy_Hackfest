class VarPrescription:
    #problem data xpath
    PROBLEM_NAME_XPATH ='//*[@id="problem_name"]'
    PROBLEM_BODY_SITE_XPATH ='//*[@id="problem_body_site"]'
    SEVERITY_XPATH ='//*[@id="severity"]'

    # problem data
    PROBLEM_NAME = 'problem1'
    PROBLEM_BODY_SITE = 'bodysite1'
    SEVERITY = 'high'

    #medicine data xpath
    ADD_MEDICINE_BTN_XPATH = '//*[@id="main-section"]/div[2]/div/div/button'
    MEDICINE_NAME_XPATH = '//*[@id="medicine_name{}"]'
    FORM_XPATH = '//*[@id="form{}"]'
    STRENGTH_XPATH = '//*[@id="strength{}"]'
    STRENGTH_UNIT_XPATH = '//*[@id="strength_unit{}"]'
    DILUENT_XPATH = '//*[@id="diluent{}"]'
    DILUENT_AMOUNT_XPATH = '//*[@id="diluent_amount{}"]'
    DILUENT_UNIT_XPATH = '//*[@id="diluent_unit{}"]'
    DOSADE_DIRECTIONS_XPATH = '//*[@id="dosade_directions{}"]'
    FREQUENCY_XPATH = '//*[@id="frequency{}"]'
    FREQUENCY_UNIT_XPATH = '//*[@id="frequency_unit{}"]'
    INTERVAL_XPATH = '//*[@id="interval{}"]'
    INTERVAL_UNIT_XPATH = '//*[@id="interval_unit{}"]'
    NAMED_TIME_EVENT_XPATH = '//*[@id="named_time_event{}"]'
    EXACT_TIMING_CRITICAL_XPATH = '//*[@id="exact_timing_critical{}"]'

    #add_medicine data
    MEDICINE_NAME = 'medicine{}'
    FORM = 'form{}'
    STRENGTH = '{}'
    STRENGTH_UNIT = 'mg{}'
    DILUENT = 'diluent{}'
    DILUENT_AMOUNT = '{}'
    DILUENT_UNIT = 'diluentunit{}'
    DOSADE_DIRECTIONS = 'dosage_directions{}'
    FREQUENCY = '{}'
    FREQUENCY_UNIT = '1/h'
    INTERVAL = '{}'
    INTERVAL_UNIT = 'h'
    NAMED_TIME_EVENT = 'named time event{}'
    SUBMIT_PRESCRIPTION='/html/body/div[1]/div[2]/div/form/input[3]'

    # Argument Click
    ARGUMENT_CLICK = "arguments[0].click();"

    