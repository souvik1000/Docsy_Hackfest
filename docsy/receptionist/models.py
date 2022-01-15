from django.db import models
from datetime import date, datetime
from patient.models import patient
from django.contrib.auth.models import AbstractUser

class doctor(models.Model):
    name = models.TextField(max_length=50)
    specalist = models.TextField(max_length=50, null=True)
    email = models.EmailField(unique=True,max_length=50)
    phoneno = models.TextField(unique=True, max_length=10)
    gender = models.TextField(max_length=10)
    password = models.TextField(max_length=25)
    clinic_address = models.TextField(max_length=150)
    registration_time = models.DateField(default=date.today)


class prescription(models.Model):
    patientId = models.ForeignKey(patient,on_delete=models.CASCADE)
    doctorId = models.ForeignKey(doctor,on_delete=models.CASCADE)
    comment = models.TextField() 


class problem(models.Model):
    prescriptionId = models.ForeignKey(prescription,on_delete=models.CASCADE)
    patientId = models.ForeignKey(patient,on_delete=models.CASCADE)
    problem_name = models.TextField() 
    problem_body_site = models.TextField() 
    severity = models.TextField()
    date_time_onset = models.DateTimeField(default=datetime.now)


class medicines(models.Model):
    prescriptionId = models.ForeignKey(prescription,on_delete=models.CASCADE)
    medicine_name = models.TextField()
    form = models.TextField()
    strength = models.IntegerField(default=0)
    strength_unit = models.TextField()
    diluent = models.TextField()
    diluent_amount = models.IntegerField(default=0)
    diluent_unit = models.TextField()
    dosade_directions = models.TextField()
    frequency = models.IntegerField(default=0)
    frequency_unit = models.TextField()
    interval = models.IntegerField(default=0)
    interval_unit = models.TextField()
    named_time_event = models.TextField()
    exact_timing_critical = models.BooleanField()
    
    
class diagnostic(models.Model):
    patientId = models.ForeignKey(patient,on_delete=models.CASCADE)
    doctorId = models.ForeignKey(doctor,on_delete=models.CASCADE)
    
    
class labreport(models.Model):
    diagnosticId = models.ForeignKey(diagnostic,on_delete=models.CASCADE)
    lab_event = models.TextField()
    lab_test_name = models.TextField()
    lab_specimen_type = models.TextField()
    lab_specimen_method = models.TextField()
    lab_specimen_body_site = models.TextField()
    lab_findings = models.TextField()
    lab_document = models.FileField(upload_to='dianosis_image/', null=True, verbose_name="")


class imagingexam(models.Model):
    diagnosticId = models.ForeignKey(diagnostic,on_delete=models.CASCADE)
    imaging_event = models.TextField()
    imaging_test_name = models.TextField()
    imaging_modality = models.TextField()
    imaging_body_site = models.TextField()
    imaging_findings = models.TextField()
    imaging_document = models.FileField(upload_to='dianosis_image/', null=True, verbose_name="")
    
class allergies(models.Model):
    patientId = models.ForeignKey(patient,on_delete=models.CASCADE)
    substance = models.TextField()
    criticality = models.TextField()
    type = models.TextField()
    comment = models.TextField()

class procedurehistory(models.Model):
    patientId = models.ForeignKey(patient,on_delete=models.CASCADE)
    procedure_name = models.TextField()
    body_site = models.TextField()
    procedure_date = models.DateField(default=date.today)
    
class illnesshistory(models.Model):
    patientId = models.ForeignKey(patient,on_delete=models.CASCADE)
    illness_name = models.TextField()
    body_site = models.TextField()
    severity = models.TextField()
    illness_date_onset = models.DateTimeField(default = datetime.now)
    illness_date_abatement = models.DateTimeField(default = datetime.now)


