from django.shortcuts import render
from django.http import HttpResponse
from .models import doctor

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
    return render(request,'historyofillness.html')    
