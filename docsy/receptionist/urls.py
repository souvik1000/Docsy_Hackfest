from os import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),

    # path('patientSummary/',views.patientsummary,name="patientsummary"),
    # path('patientSummary/allergies',views.allergies,name="allergies"),
    # path('patientSummary/historyofillness',views.historyofillness,name="historyofillness"),
    path('prescription/',views.doctorprescription,name="doctorprescription"),
    path('prescriptionBackend/',views.prescriptionBackend,name="prescriptionBackend"),
    
    path('patientSummary/', views.patientSummary, name="patientSummary"),
    path('createPartionData/', views.createPartionData, name="createPartionData"),
    path('patientIllnessCreation/', views.patientIllnessCreation, name="patientIllnessCreation"),
    path('patientAllergiesCreation/', views.patientAllergiesCreation, name="patientAllergiesCreation"),
    path('historyofillness/', views.historyofillness, name="historyofillness"),
    path('patientIllnessView/', views.patientIllnessView, name="patientIllnessView"),
    
    path('logout/',views.logout,name="logout"),
]