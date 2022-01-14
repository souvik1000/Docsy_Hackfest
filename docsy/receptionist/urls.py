from os import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),
    path('prescription/<str:patientid>/<str:appointmentId>',views.doctorprescription,name="doctorprescription"),
    path('prescriptionBackend/',views.prescriptionBackend,name="prescriptionBackend"),
    path('logout/',views.logout,name="logout"),
    path('patientSummary/procedure',views.procedure,name="procedure"),
    path('procedurecreation/',views.procedurecreation,name="procedurecreation"),
    path('patientSummary/', views.patientSummary, name="patientSummary"),
    path('doctorsDashboard/createPatientData/<str:patientid>/<str:appointmentId>', views.createPatientData, name="createPatientData"),
    path('patientIllnessCreation/', views.patientIllnessCreation, name="patientIllnessCreation"),
    path('patientAllergiesCreation/', views.patientAllergiesCreation, name="patientAllergiesCreation"),
    path('patientSummaryView/', views.patientSummaryView, name="patientSummaryView"),
    path('diaganosisReportCreation', views.diaganosisReportCreation, name="diaganosisReportCreation"),
    # path('labreportView/',views.labreportView, name="labreportView"),
    path('doctorsDashboard/checkstatus/<str:pid>/<str:appid>', views.checkstatus, name="checkstatus"),
    # path('patientIllnessView/', views.patientIllnessView, name="patientIllnessView"),
    # path('allergyview/', views.allergyview, name="allergyview"),
    path('logout/',views.logout,name="logout"),
    path("doctoremailalreadyexists/",views.doctoremailalreadyexists,name="doctoremailalreadyexists"),
    path("doctormobilealreadyexists/",views.doctormobilealreadyexists,name="doctormobilealreadyexists")

]