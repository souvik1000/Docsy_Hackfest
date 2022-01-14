from django.http.response import HttpResponse
from django.shortcuts import render
from .models import patient

# Create your views here.
def patientLogin(request):
    return render(request,'patientLogin.html')

def patientregistrationValidation(request):
    name = request.POST['name']
    dob=request.POST['dob']
    email=request.POST['email']
    gender = request.POST['gender']
    phone = request.POST['phone']
    password = request.POST['password']
    submit_details=patient(name=name,dob=dob,email=email,gender=gender,phoneno=phone,password=password)
    submit_details.save()
    return render(request,'patientLogin.html',{'message':'register success'})
    

def patientloginauth(request):
    email=request.POST['a']
    passw=request.POST['b']
    patient_table=patient.objects.all()
    for i in patient_table:
        if(i.email==email and i.password==passw):
            request.session['patient_id'] = i.id
            return  HttpResponse(1)
    return HttpResponse(0)

def emailalreadyexists(request):
    email=request.POST['a']
    patient_table=patient.objects.all()
    for i in patient_table:
        if(i.email==email):
            return  HttpResponse(0)
    return HttpResponse(1)
def mobilealreadyexists(request):
    mobile=request.POST['a']
    patient_table=patient.objects.all()
    for i in patient_table:
        if(i.mobileno==mobile):
            return  HttpResponse(0)
    return HttpResponse(1)
def patientDashboard(request):
    if 'patient_id' in request.session:
        return HttpResponse(request.session['patient_id'])
    return HttpResponse("patient dashboard")

def logout(request):
    if request.session.get('doctor_id', True):
            del request.session['doctor_id']
            return redirect(login)