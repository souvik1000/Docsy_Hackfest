from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import doctor,problem,medicines,prescription, illnesshistory,allergies,procedurehistory
from patient.models import patient

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
        return redirect

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
    return render(request,'doctorsDashboard.html')
    return HttpResponse("Doctors Dashboard")

def patientsummary(request):
    return render (request,'patientsummary.html')
 
def allergies(request):
    return render (request,'allergies.html')

def procedurecreation(request):
    patientId=patient.objects.get(id=1)
    procedure_name=request.POST['Procedure']
    body_site=request.POST['BodySite']
    date_of_procedure=request.POST['DateofProcedure']
    submit_procedure=procedurehistory(patientId=patientId,procedure_name=procedure_name ,body_site=body_site,procedure_date=date_of_procedure)
    submit_procedure.save()       
    return HttpResponse("Added Successful")

def procedure(request):
    return render(request,'procedure.html' )
 

def historyofillness(request):
    return render(request, 'historyofillness.html')

def patientSummary(request):
    return render(request,'patientsummary.html')

def createPartionData(request):
    return render(request, 'createPartionData.html')

def patientAllergiesCreation(request):
    patientId = request.POST['patientId']
    substance = request.POST['substance']
    criticality = request.POST['criticality']
    type = request.POST['type']
    comment = request.POST['comment']
    pid = patient.objects.get(id=patientId)
    allergies(patientId=pid, substance=substance, criticality=criticality, type=type, comment=comment).save()
    return render(request, 'createPartionData.html')
 
def patientIllnessCreation(request):
    patientno = request.POST['patientno']
    illness_name = request.POST['illness_name']
    body_site = request.POST['body_site']
    severity = request.POST['severity']
    illness_date_onset = request.POST['illness_date_onset']
    illness_date_abatement = request.POST['illness_date_abatement']
    pid = patient.objects.get(id=patientno)
    submit_details = illnesshistory(patientId=pid, illness_name=illness_name, body_site=body_site, severity=severity, illness_date_onset=illness_date_onset, illness_date_abatement=illness_date_abatement)
    submit_details.save()
    return render(request, 'createPartionData.html')

def patientIllnessView(request):
    patient_data = patient.objects.filter(name="Souvik", phoneno="8450042512")
    patient_id = patient_data[0].id
    illness_data = illnesshistory.objects.all().filter(patientId=patient_id)
    # print(illness_data[0].illness_name)
    return render(request, 'patientsummary.html', {"illness_data":illness_data})
    # return render()

def allergyview(request):
    patient_data=patient.objects.filter(name="Souvik",phoneno="8450042512")
    patient_id=patient_data[0].id
    allergy_data=allergies.objects.all().filter(patientId=patient_id)
    return render(request,'patientsummary.html',{"allergy_data":allergy_data})
# def digenosisCreation(request):
#     lab_event = 
#     lab_test_name = 
#     lab_specimen_type = 
#     lab_specimen_method = 
#     lab_specimen_body_site = 
#     lab_findings = 
#     upload_file = 


# def diagenosisLink(request):
#     return render()


def logout(request):
    if request.session.get('doctor_id', True):
            del request.session['doctor_id']
            return redirect(login)
