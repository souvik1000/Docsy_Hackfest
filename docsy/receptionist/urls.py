from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),
    path('patientsummary/',views.patientsummary,name="patientsummary"),
    path('patientSummary/allergies',views.allergies,name="allergies")
]