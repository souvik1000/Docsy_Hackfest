from django.test import TestCase
from patient.models import patient,Appointment
# from receptionist.models import doctor,diagnostic,labreport,imagingexam, medicines, prescription,problem,allergies,procedurehistory,illnesshistory


class PatientTestCase(TestCase):
    def test1_field_patient_creation(self):
        self.register_as_patient = patient.objects.create(name="pavan",dob='1999-11-18',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        self.assertTrue(isinstance(self.register_as_patient, patient))
    
    def test2_appointment_creation(self):
        p=patient.objects.create(name="pavan",dob='1999-11-18',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        patient_obj=patient.objects.get(id=p.id)
        self.create_appointment=Appointment.objects.create(patientId=patient_obj,specalist="ENT",doctorId=2,appointmentTime="2022-01-01 18:05:00+00:00",disease="corona")
        self.assertTrue(isinstance(self.create_appointment, Appointment))
