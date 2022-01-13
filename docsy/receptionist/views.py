from django.shortcuts import render
from django.http import HttpResponse

from patient.models import patient
from .models import doctor,illnesshistory

def login(request):
    return render(request,'login.html')

def registrationValidation(request):
    name = request.POST['name']
    email=request.POST['email']
    specalist = request.POST['specality']
    gender = request.POST['gender']
    phone = request.POST['phone']
    password = request.POST['password']
    clinic_address = request.POST['clinic_address']
    submit_details=doctor(name=name,specalist=specalist,email=email,gender=gender,phoneno=phone,password=password,clinic_address=clinic_address)
    submit_details.save()
    return HttpResponse("Registration Successful")

def loginauth(request):
    phone=request.POST['a']
    passw=request.POST['b']
    doctors_table=doctor.objects.all()
    for i in doctors_table:
        if(i.phone==phone and i.password==passw):
            return  HttpResponse(1)
    return HttpResponse(0)

def doctorsDashboard(request):
    return HttpResponse("Doctors Dashboard")

def patientsummary(request):
    return render (request,'patientsummary.html')
 
def allergies(request):
    return render (request,'allergies.html')

def historyofillness(request):
    return render(request, 'historyofillness.html')

def patientIllnessCreation(request):
    patientno = request.POST['patientno']
    illness_name = request.POST['illness_name']
    body_site = request.POST['body_site']
    severity = request.POST['severity']
    illness_date_onset = request.POST['illness_date_onset']
    illness_date_abatement = request.POST['illness_date_abatement']
    pid = patient.objects.get(id=patientno)
    # print(patientno, illness_name, body_site, severity, illness_date_onset, illness_date_abatement)
    submit_details = illnesshistory(patientId=pid, illness_name=illness_name, body_site=body_site, severity=severity, illness_date_onset=illness_date_onset, illness_date_abatement=illness_date_abatement)
    submit_details.save()
    return HttpResponse("Added Successful")

# def labreportCreation(request):
    