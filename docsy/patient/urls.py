from django.urls import path
from . import views

urlpatterns=[
    path('',views.patientLogin,name="patientLogin"),
    path('patientregistrationValidation/',views.patientregistrationValidation,name='patientregistrationValidation'),
    path('patientloginauth/',views.patientloginauth,name="patientloginauth"),
    path('patientDashboard/',views.patientDashboard,name="patientDashboard"),
    path("emailalreadyexists/",views.emailalreadyexists,name="emailalreadyexists"),
    path("mobilealreadyexists/",views.mobilealreadyexists,name="mobilealreadyexists"),
    path('patientAppointment/',views.patientAppointment,name="patientAppointment"),
    path('patientAppointmentBackend/',views.patientAppointmentBackend,name="patientAppointmentBackend"),
    path('getspecialiseddoctor/',views.getspecialiseddoctor,name="getspecialiseddoctor")]