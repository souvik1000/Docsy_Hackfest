from enum import unique
from django.db import models

from datetime import datetime,date
# Create your models here.

class patient(models.Model):
    name = models.TextField(max_length=50)
    dob = models.DateField(default=date.today)
    gender = models.TextField(max_length=20)
    phoneno = models.TextField(unique=True, max_length=10)
    email=models.EmailField(unique=True,max_length=50)
    password = models.TextField(max_length=25)
    address = models.TextField(max_length=150)
    registration_time = models.DateField(default=date.today)


class Appointment(models.Model):
    patientId= models.ForeignKey(patient,on_delete=models.CASCADE)
    doctorId = models.IntegerField()
    # doctorId =models.ForeignKey(doctor,on_delete=models.CASCADE)
    specalist = models.TextField(max_length=50, null=True)
    disease=models.TextField(max_length=50, null=True)
    appointmentTime=models.DateTimeField(default=datetime.now)
    status=models.TextField(default="0")

    