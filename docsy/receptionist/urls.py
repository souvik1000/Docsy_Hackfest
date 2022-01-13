from os import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),
<<<<<<< HEAD
<<<<<<< HEAD
    path('patientSummary/',views.patientsummary,name="patientsummary"),
    path('patientSummary/allergies',views.allergies,name="allergies"),
    path('patientSummary/historyofillness',views.historyofillness,name="historyofillness")
=======
<<<<<<< HEAD
=======
>>>>>>> dc11eafb9ac38c9280b907e558e7f10f5128d155
    path('prescription/',views.doctorprescription,name="doctorprescription"),
    path('prescriptionBackend/',views.prescriptionBackend,name="prescriptionBackend"),
    
    path('patientSummary/', views.patientSummary, name="patientSummary"),
    path('createPartionData/', views.createPartionData, name="createPartionData"),
    path('patientIllnessCreation/', views.patientIllnessCreation, name="patientIllnessCreation"),
    path('patientAllergiesCreation/', views.patientAllergiesCreation, name="patientAllergiesCreation"),
    path('historyofillness/', views.historyofillness, name="historyofillness"),
    path('patientIllnessView/', views.patientIllnessView, name="patientIllnessView"),
    
    path('logout/',views.logout,name="logout")
<<<<<<< HEAD
=======

<<<<<<< HEAD
=======
    path('patientSummary/',views.patientsummary,name="patientsummary"),
    path('patientSummary/allergies',views.allergies,name="allergies"),
    path('patientSummary/historyofillness', views.historyofillness, name="historyofillness"),
    path('patientSummary/patientIllnessCreation', views.patientIllnessCreation, name="patientIllnessCreation")
>>>>>>> 0b1e69d824fe2b10dcc90d6c560c700dfc632c85
>>>>>>> d397ea26ccacc0d02cc4cfabdb2e6b46875634f4
=======
>>>>>>> dc11eafb9ac38c9280b907e558e7f10f5128d155
>>>>>>> b118481a95b66a26239a9a6687eef668ab18a76b
]