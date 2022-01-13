from django.shortcuts import render,redirect
from django.http import HttpResponse
<<<<<<< HEAD
from .models import doctor,problem,medicines,prescription
from patient.models import patient
=======
from .models import doctor,illnesshistory
>>>>>>> 0b1e69d824fe2b10dcc90d6c560c700dfc632c85

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
        if(i.phoneno==phone and i.password==passw):
            request.session['doctor_id'] = i.id
            return  HttpResponse(1)
    return HttpResponse(0)

def doctorprescription(request):
    if 'doctor_id' in request.session:
        return render(request,'prescription.html')
    else:
        return redirect(login)

def prescriptionBackend(request):
    if 'doctor_id' in request.session:
            doctorid=request.session['doctor_id']
            doctorObj=doctor.objects.get(id=doctorid)
            #retrieve doctorid through
            patientId=request.POST['patientId']
            patientObj=patient.objects.get(id=patientId)
            # return HttpResponse(patientObj.id)
            prescription_data=prescription(comment='hii',doctorId=doctorObj,patientId=patientObj)
            prescription_data.save()

            prescriptionId=prescription.objects.get(id=prescription_data.id)
            problem_name=request.POST['problem_name']
            problem_body_site=request.POST['problem_body_site']
            severity=request.POST['severity']
            problems_data=problem(prescriptionId=prescriptionId,patientId=patientObj,problem_name=problem_name,problem_body_site=problem_body_site,severity=severity)
            problems_data.save()

            l1=[]
            medicine_count=request.POST['medicine_count']
            for k in range(1,int(medicine_count)+1):
                i=str(k)
                medicine_name=request.POST['medicine_name'+i]
                form=request.POST['form'+i]
                strength=request.POST['strength'+i]
                strength_unit=request.POST['strength_unit'+i]
                diluent=request.POST['diluent'+i]
                diluent_amount=request.POST['diluent_amount'+i]
                diluent_unit=request.POST['diluent_unit'+i]
                dosade_directions=request.POST['dosade_directions'+i]
                frequency=request.POST['frequency'+i]
                frequency_unit=request.POST['frequency_unit'+i]
                interval=request.POST['interval'+i]
                interval_unit=request.POST['interval_unit'+i]
                named_time_event=request.POST['named_time_event'+i]


                
                if len(request.POST.getlist('exact_timing_critical'+i))==0:
                    exact_timing_critical=0
                else:
                    exact_timing_critical=1
                
                medicine_data=medicines(prescriptionId=prescriptionId,medicine_name=medicine_name,form=form,strength=strength,strength_unit=strength_unit,diluent=diluent,diluent_amount=diluent_amount,diluent_unit=diluent_unit,dosade_directions=dosade_directions,frequency=frequency,frequency_unit=frequency_unit,interval=interval,interval_unit=interval_unit,named_time_event=named_time_event,exact_timing_critical=exact_timing_critical)
                medicine_data.save()
                l1.append([medicine_name,form,strength,strength_unit,diluent,diluent_amount,diluent_unit,dosade_directions,frequency,frequency_unit,interval,interval_unit,named_time_event,exact_timing_critical])
            return HttpResponse("Prescription added")
    else:
        return redirect(login)

    return HttpResponse(l1)

   


def doctorsDashboard(request):
    return HttpResponse("Doctors Dashboard")

<<<<<<< HEAD
def logout(request):
    if request.session.get('doctor_id', True):
            del request.session['doctor_id']
            return redirect(login)
    
=======
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
    print(patientno, illness_name, body_site, severity, illness_date_onset, illness_date_abatement)
    submit_details = illnesshistory(patientId=patientno, illness_name=illness_name, body_site=body_site, severity=severity, illness_date_onset=illness_date_onset, illness_date_abatement=illness_date_abatement)
    submit_details.save()
    return HttpResponse("Added Successful")
>>>>>>> 0b1e69d824fe2b10dcc90d6c560c700dfc632c85
