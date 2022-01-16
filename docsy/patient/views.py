from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import patient,Appointment
from receptionist.models import doctor,diagnostic,labreport,imagingexam, medicines, prescription

# Create your views here.
def patientHomePage(request):
    if 'patient_id' in request.session:
        patient_id=request.session['patient_id']
        patient_data=patient.objects.get(id=patient_id)
        diagnostic_data = diagnostic.objects.all().filter(patientId=patient_id)
        lab_reports = []
        image_reports=[]
        for data in range(0, len(diagnostic_data)):
            lab_reports.append(labreport.objects.get(diagnosticId=diagnostic_data[data].id))
            image_reports.append(imagingexam.objects.get(diagnosticId=diagnostic_data[data].id))
        return render(request,'patientHomePage.html',{"patient_data":patient_data,"diagnostic_data":diagnostic_data,"lab_reports":lab_reports,"image_reports":image_reports})
    else:
        return redirect(patientLogin)
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
        if(i.phoneno==mobile):
            return  HttpResponse(0)
    return HttpResponse(1)

def patientDashboard(request):
    if 'patient_id' in request.session:
        return HttpResponse(request.session['patient_id'])
    return HttpResponse("patient dashboard")

def patientAppointment(request): 
    all_specialization=doctor.objects.values('specalist')
    # return HttpResponse(all_specialization)
    return render(request,'patientAppointment.html',{'all_specialization':all_specialization})

def getspecialiseddoctor(request):
    specalization=request.POST['spec']
    doctors_by_specalization=""
    specialzed_doctors=doctor.objects.filter(specalist=specalization)
    for i in specialzed_doctors:
        doctors_by_specalization="<option value="+str(i.id)+">"+i.name+"</option>"
    return HttpResponse(doctors_by_specalization)

def patientAppointmentBackend(request):
    patient_id=request.session['patient_id']
    pid=patient.objects.get(id=patient_id)
    specalization=request.POST['specalization']
    Doctor=int(request.POST['Doctor'])
    appointmentTime=request.POST['appointmentTime']
    disease=request.POST['disease']
    # return HttpResponse(patient_id)
    submit_details=Appointment(patientId=pid,specalist=specalization,doctorId=Doctor,appointmentTime=appointmentTime,disease=disease)
    submit_details.save()
    return HttpResponse('Appointment booked at {}'.format(appointmentTime))

def patientDashboard(request):
    if 'patient_id' in request.session:
        return HttpResponse("Patient dashboard "+str(request.session['patient_id'])) 
    else:
        return redirect(patientLogin)
        # return HttpResponse("Please login.")

def patientlogout(request):
    if request.session.get('patient_id', True):
            del request.session['patient_id']
            return redirect(patientLogin)