from django.db import models
from datetime import datetime,date
# Create your models here.

class patient(models.Model):
    name = models.TextField(max_length=100)
    dob = models.DateField(default=date.today)
    gender = models.TextField()
    phoneno = models.TextField()
    email=models.EmailField(unique=True,max_length=200)
    address = models.TextField()
    registration_time = models.DateField(default=date.today)
    
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
 
