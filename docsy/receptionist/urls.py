from os import name
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),
    path('prescription/<str:patientid>/<str:appointmentId>',views.doctorprescription,name="doctorprescription"),
    path('prescriptionBackend/',views.prescriptionBackend,name="prescriptionBackend"),
    path('patientSummary/procedure',views.procedure,name="procedure"),
    path('procedurecreation/',views.procedurecreation,name="procedurecreation"),
    path('doctorsDashboard/patientSummaryView/<str:pid>/<str:appid>', views.patientSummaryView, name="patientSummaryView"),
    path('doctorsDashboard/add_reports/<str:patientid>/<str:appointmentId>', views.add_reports, name="add_reports"),
    path("doctoremailalreadyexists/",views.doctoremailalreadyexists,name="doctoremailalreadyexists"),
    path("doctormobilealreadyexists/",views.doctormobilealreadyexists,name="doctormobilealreadyexists"),
    path('doctorsDashboard/checkstatus/<str:pid>/<str:appid>', views.checkstatus, name="checkstatus"),
    
    
    path('patientSummary/',views.patientSummary,name="patientSummary"),
    path('createPatientData/',views.createPatientData,name="createPatientData"),
    
    path('patientIllnessCreation/', views.patientIllnessCreation, name="patientIllnessCreation"),
    path('patientAllergiesCreation/', views.patientAllergiesCreation, name="patientAllergiesCreation"),
    path('patientSummaryView/', views.patientSummaryView, name="patientSummaryView"),
    path('diaganosisReportCreation', views.diaganosisReportCreation, name="diaganosisReportCreation"),
    path('logout/',views.logout,name="logout"),
<<<<<<< HEAD
    # path('viewpresciptions',views.viewpresciption,name="prescription"),
    path("doctoremailalreadyexists/",views.doctoremailalreadyexists,name="doctoremailalreadyexists"),
    path("doctormobilealreadyexists/",views.doctormobilealreadyexists,name="doctormobilealreadyexists")
=======
]
>>>>>>> a0395c5f9076fa1913630f70a4c28b4f8f0798f5

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)