# from django.contrib.admin.decorators import register
from datetime import date,datetime
from django.db import models
from patient.models import patient

class doctor(models.Model):
    name = models.TextField(max_length=100)
    specalist = models.TextField(max_length=100, null=True)
    password = models.TextField(max_length=1000)
    email=models.EmailField(unique=True,max_length=200)
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
    strength = models.IntegerField()
    strength_unit = models.TextField()
    diluent = models.TextField()
    diluent_amount = models.IntegerField()
    diluent_unit = models.TextField()
    dosade_directions = models.TextField()
    frequency = models.IntegerField()
    frequency_unit = models.TextField()
    interval = models.IntegerField()
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
    lab_document = models.FileField(upload_to='images/', null=True, verbose_name="")


class imagingexam(models.Model):
    diagnosticId = models.ForeignKey(diagnostic,on_delete=models.CASCADE)
    imaging_event = models.TextField()
    imaging_test_name = models.TextField()
    imaging_modality = models.TextField()
    imaging_body_site = models.TextField()
    imaging_findings = models.TextField()
    imaging_document = models.FileField(upload_to='images/', null=True, verbose_name="")
    