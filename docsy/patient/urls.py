from django.urls import path
from . import views

urlpatterns=[
    path('',views.patientHomePage,name="patientHomePage"),
    path('patientlogin/',views.patientLogin,name="patientLogin"),
    path('patientregistrationValidation/',views.patientregistrationValidation,name='patientregistrationValidation'),
    path('patientloginauth/',views.patientloginauth,name="patientloginauth"),
    path('patientDashboard/',views.patientDashboard,name="patientDashboard"),
    path("emailalreadyexists/",views.emailalreadyexists,name="emailalreadyexists"),
    path("mobilealreadyexists/",views.mobilealreadyexists,name="mobilealreadyexists"),
    path('patientAppointment/',views.patientAppointment,name="patientAppointment"),
    path('patientAppointmentBackend/',views.patientAppointmentBackend,name="patientAppointmentBackend"),
    path('getspecialiseddoctor/',views.getspecialiseddoctor,name="getspecialiseddoctor"),    
    path('patientPrescription/',views.patientPrescription,name="patientPrescription"),
    path('patientprescription/<str:prescription_id>',views.patientprescription,name="patientprescription"),
    
    path('downloadLabReports/<str:report>/<str:reportid>',views.downloadLabReports,name="downloadLabReports"),
    path('patientlogout/',views.patientlogout,name="patientlogout")
    ]