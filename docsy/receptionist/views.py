# from curses.ascii import HT
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date

# from .models import doctor,problem,medicines,prescription
from patient.models import patient,Appointment  
from .models import prescription
from .models import doctor,problem,medicines,prescription, illnesshistory,allergies,procedurehistory,diagnostic,labreport,imagingexam


def login(request):
    return render(request,'login.html')

def doctoremailalreadyexists(request):
    email=request.POST['a']
    patient_table=patient.objects.all()
    for i in patient_table:
        if(i.email==email):
            return  HttpResponse(0)
    return HttpResponse(1)

def doctormobilealreadyexists(request):
    mobile=request.POST['a']
    patient_table=patient.objects.all()
    for i in patient_table:
        if(i.phoneno==mobile):
            return  HttpResponse(0)
    return HttpResponse(1)

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
    return render(request, 'login.html')

def loginauth(request):
    phone=request.POST['a']
    passw=request.POST['b']
    doctors_table=doctor.objects.all()
    for i in doctors_table:
        if(i.phoneno==phone and i.password==passw):
            request.session['doctor_id'] = i.id
            return  HttpResponse(1)
    return HttpResponse(0)

def doctorprescription(request,patientid,appointmentId):
    if 'doctor_id' in request.session:
        appointment=Appointment.objects.get(id=appointmentId)
        #ekkada chudu
        appointment.status="0"
        appointment.save()
        return render(request,'prescription.html',{'patientid':patientid})
    else:
        return redirect("login")

def prescriptionBackend(request):
    if 'doctor_id' in request.session:
        try:
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
            return redirect(doctorsDashboard)
            # return HttpResponse("Prescription added")
        except:
            return redirect(doctorsDashboard)
    else:
        return redirect(login)

def add_reports(request,patientid,appointmentId):
    add_reports.pid,add_reports.appid=patientid,appointmentId
    # return HttpResponse(add_reports.pid)
    return render(request, 'add_reports.html',{'patientid':patientid,'appointmentId':appointmentId})

def checkstatus(requst,pid,appid):
    appointment=Appointment.objects.get(id=appid)
    #ekkada chudu
    appointment.status="1"
    appointment.save()
    return redirect(doctorsDashboard)

def homePage(request):
    if 'doctor_id' in request.session:
        doctor_id=doctor.objects.get(id=request.session['doctor_id'])
        return render(request, 'index.html', {"doctor_id":doctor_id})
    else:
        return redirect("login")

def doctorsDashboard(request):
    doctor_id=request.session['doctor_id']
    today_appointments=Appointment.objects.all()
    d=doctor.objects.get(id=doctor_id)
    a=Appointment.objects.filter(doctorId=d.id,status="0")
    ap=[]
    for i in a:
        x=i.patientId
        ap.append([x.id,x.name,i.disease,i.appointmentTime,i.id])

    b=Appointment.objects.filter(doctorId=d.id,status="1")
    bp=[]
    for i in b:
        x=i.patientId
        bp.append([x.id,x.name,i.disease,i.appointmentTime,i.id])
    return render(request,'doctorsDashboard.html',{"today_appointments":ap,"past_appointments":bp, "doctor_id":d})

def procedure(request):
    return render(request,'procedure.html')

# def createPatientData(request,patientid,appointmentId):
#     return render(request, 'createPatientData.html',{'patientid':patientid,'appointmentId':appointmentId})

# For Creation 
def createPatientData(request):
    return render(request, 'createPatientData.html')

def patientDetail(request):
    if 'doctor_id' in request.session:
        doctor_id=doctor.objects.get(id=request.session['doctor_id'])
        return render(request, 'patientDetailsForm.html', {"doctor_id":doctor_id})
    else:
        return redirect("login")

def patientDetails(request):
    patient_name = request.POST['patient_name']
    patient_number = request.POST['phone_number']
    patient_id = patient.objects.filter(name__istartswith=patient_name, phoneno=patient_number)
    # patient_id = patient_data[0].id
    # pid = patient.objects.get(id=patient_id)
    
    substance = request.POST['substance']
    criticality = request.POST['criticality']
    type = request.POST['type']
    comment = request.POST['comment']
    
    procedure_name=request.POST['Procedure']
    body_site=request.POST['BodySite']
    date_of_procedure=request.POST['DateofProcedure']
    
    illness_name = request.POST['illness_name']
    body_site = request.POST['body_site']
    severity = request.POST['severity']
    illness_date_onset = request.POST['illness_date_onset']
    illness_date_abatement = request.POST['illness_date_abatement']
    
    # Adding to DB based on data provided by receptionist
    if (substance!=''):
        allergies(patientId=patient_id, substance=substance, criticality=criticality, type=type, comment=comment).save()
        
    if (procedure_name != '') and (date_of_procedure != ''):
        procedurehistory(patientId=patient_id,procedure_name=procedure_name ,body_site=body_site,procedure_date=date_of_procedure).save()
        
    if (illness_name != '') and (illness_date_onset != '') and (illness_date_abatement != ''):
        illnesshistory(patientId=patient_id, illness_name=illness_name, body_site=body_site, severity=severity, illness_date_onset=illness_date_onset, illness_date_abatement=illness_date_abatement).save()
        
    return render(request, 'patientDetailsForm.html')

def imageView(request,pid, imagepath, dirname, data):
    concatedImagePath = dirname + "/" + data
    return render(request, "imageViewPage.html", {"imageData":str(concatedImagePath)})


# doctordashboard-->add_reports/pid/apid-->add_reports.html--->diaganosisReportCreation
def diaganosisReportCreation(request):
    # patient_name = request.POST['patient_name']
    # patient_number = request.POST['phone_number']
    # doctor_name = request.POST['doctor_name']
    # doctor_number = request.POST['doctor_number']
    # patient_data = patient.objects.filter(name__istartswith=patient_name, phoneno=patient_number)
    # patient_id = patient_data[0].id
    # doctor_data = doctor.objects.filter(name__istartswith=doctor_name, phoneno=doctor_number)
    # doctor_id = doctor_data[0].id
    # try:
    # a=add_reports.pid
    patientid = patient.objects.get(id=add_reports.pid)
    # return HttpResponse(patientid)
    did=request.session['doctor_id']
    doctorid = doctor.objects.get(id=did)
    # print(patientid,doctorid)
    diagnostic_data = diagnostic(patientId=patientid, doctorId=doctorid)
    diagnostic_data.save()
    diagnosticId = diagnostic.objects.get(id=diagnostic_data.id)
    
    # hidden counter
    lab_counter = request.POST['lab_counter']
    image_counter = request.POST['image_counter']
    
    for lc in range(1,int(lab_counter)+1):
        i = str(lc)
        lab_event = request.POST['lab_event'+i]
        lab_test_name = request.POST['lab_test_name'+i]
        lab_specimen_type = request.POST['lab_specimen_type'+i]
        lab_specimen_method = request.POST['lab_specimen_method'+i]
        lab_specimen_body_site = request.POST['lab_specimen_body_site'+i]
        lab_findings = request.POST['lab_findings'+i]
        lab_document = request.FILES['lab_document'+i]
        labreport(diagnosticId=diagnosticId, lab_event=lab_event, lab_test_name=lab_test_name, lab_specimen_type=lab_specimen_type, lab_specimen_method=lab_specimen_method, lab_specimen_body_site=lab_specimen_body_site, lab_findings=lab_findings, lab_document=lab_document).save()
        
    for xc in range(1,int(image_counter)+1):
        i = str(xc)
        imaging_event=request.POST['imaging_event'+i]
        imaging_test_name=request.POST['imaging_test_name'+i]
        imaging_modality=request.POST['imaging_modality'+i]
        imaging_body_site=request.POST['imaging_body_site'+i]
        imaging_findings=request.POST['imaging_findings'+i]
        imaging_document= request.FILES['imaging_document'+i] 
        imagingexam(diagnosticId=diagnosticId,imaging_event=imaging_event, imaging_test_name=imaging_test_name, imaging_modality=imaging_modality, imaging_body_site=imaging_body_site, imaging_findings=imaging_findings, imaging_document=imaging_document).save()
        
    return redirect(doctorsDashboard)
    # except:
    #     return render(request, 'not_found_page.html', {"render_value":True})



# For Patient Data Views
def patientSummary(request):
    return render(request,'patientsummary.html')

def patientSummaryView(request,pid,appid):
    doctor_id=doctor.objects.get(id=request.session['doctor_id'])
    try:
        # Gathering Current To Previous Data
        patient_id=patient.objects.get(id=pid)
        illness_data = illnesshistory.objects.all().filter(patientId=patient_id)[::-1]
        allergy_data = allergies.objects.all().filter(patientId=patient_id)[::-1]
        procedure_data = procedurehistory.objects.all().filter(patientId=patient_id)[::-1]
        prescription_data=prescription.objects.all().filter(patientId=patient_id)[::-1]
        diagnostic_data = diagnostic.objects.all().filter(patientId=patient_id)[::-1]
        
        # Collecting Medicine based on problems
        problem_with_medicines = [];
        
        for i in prescription_data:
            sample_data = [problem.objects.get(prescriptionId=i.id), medicines.objects.filter(prescriptionId=i.id)]
            problem_with_medicines.append(sample_data)
        
        # Age Calculator
        born = patient_id.dob
        today = date.today()
        patient_age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        # Collecting data based on diagnostic_data
        all_details = []
        
        for data in range(0, len(diagnostic_data)   ):
            sample_data = [diagnostic_data[data].doctorId, labreport.objects.filter(diagnosticId=diagnostic_data[data].id), imagingexam.objects.filter(diagnosticId=diagnostic_data[data].id)]
            all_details.append(sample_data)
            
        return render(request, 'patientsummary.html', {"doctor_id":doctor_id, "problem_with_medicines":problem_with_medicines, "all_details":all_details, "patient_age":patient_age, "illness_data":illness_data, "allergy_data":allergy_data, "procedure_data":procedure_data, "patient_details":patient_id})
    except:
        return render(request, 'not_found_page.html')

def logout(request):
    if request.session.get('doctor_id', True):
            del request.session['doctor_id']
            return redirect(login)
