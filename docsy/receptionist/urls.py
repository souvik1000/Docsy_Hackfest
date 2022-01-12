from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),
    path('prescription/', views.prescription, name="prescription"),
    path('patientSummary/', views.patientSummary, name='patientSummary'),
    path('patientSummary/historyOfIllness', views.historyofillness, name='historyofillness')
]