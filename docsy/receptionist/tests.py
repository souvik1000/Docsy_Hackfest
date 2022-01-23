from django.test import TestCase
from patient.models import patient
from receptionist.models import doctor,diagnostic,labreport,imagingexam, medicines, prescription,problem,allergies,procedurehistory,illnesshistory

class DoctorTestCase(TestCase):
    def test3_doctor_creation(self):
        self.register_as_doctor=doctor.objects.create(name="pavan",specalist="ENT",email="pavan@gmail.com",gender="male",phoneno="7981151302",password="Doctor@123",clinic_address="none")
        self.assertTrue(isinstance(self.register_as_doctor, doctor))

    def test4_doctor_add_prescription(self):
        p=patient.objects.create(name="pavan",dob='1999-11-18',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        patient_obj=patient.objects.get(id=p.id)
        d=doctor.objects.create(name="pavan",specalist="ENT",email="pavan@gmail.com",gender="male",phoneno="7981151302",password="Doctor@123",clinic_address="none")
        doctor_obj=doctor.objects.get(id=d.id)
        
        #add prescription
        self.add_prescription=prescription.objects.create(comment='hii',doctorId=doctor_obj,patientId=patient_obj)
        prescription_obj=prescription.objects.get(id=self.add_prescription.id)
        #add problem to particular prescription
        self.add_problem=problem.objects.create(prescriptionId=prescription_obj,patientId=patient_obj,problem_name="problem 1",problem_body_site="body site 1",severity="high",date_time_onset='2022-01-18 18:05:00+00:00')
        #add medicines to particular prescription

        self.add_medicine=medicines.objects.create(prescriptionId=prescription_obj,medicine_name='medicine_1',form='form',strength=1,strength_unit='strength_unit',diluent='diluent',diluent_amount=2,diluent_unit='diluent_unit',dosade_directions='dosade_directions',frequency=3,frequency_unit='frequency_unit',interval=5,interval_unit='interval_unit',named_time_event='named_time_event',exact_timing_critical=True)

        self.assertTrue(isinstance(self.add_prescription, prescription))
        self.assertTrue(isinstance(self.add_problem,problem))
        self.assertTrue(isinstance(self.add_medicine,medicines))

    def test5_allergies(self):
        p=patient.objects.create(name="pavan",dob='1999-11-18',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        patient_obj=patient.objects.get(id=p.id)
        self.create_allergies=allergies.objects.create(patientId=patient_obj, substance='substance', criticality='criticality', type='type', comment='comment')
        self.assertTrue(isinstance(self.create_allergies, allergies))

    def test6_procedurehistory(self):
        p=patient.objects.create(name="pavan",dob='1999-11-18',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        patient_obj=patient.objects.get(id=p.id)
        self.create_procedurehistory=procedurehistory.objects.create(patientId=patient_obj,procedure_name='procedure_name' ,body_site='body_site',procedure_date='1999-11-18')
        self.assertTrue(isinstance(self.create_procedurehistory, procedurehistory))
    def test7_illnesshistory(self):
        p=patient.objects.create(name="pavan",dob='1999-11-12',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        patient_obj=patient.objects.get(id=p.id)
        self.create_illnesshistory=illnesshistory.objects.create(patientId=patient_obj, illness_name='illness_name', body_site='body_site', severity='severity', illness_date_onset='2021-02-10 18:05:00+00:00', illness_date_abatement='2022-01-18 18:05:00+00:00')
        self.assertTrue(isinstance(self.create_illnesshistory, illnesshistory))
    
    def test8_diagnostics(self):
        p=patient.objects.create(name="pavan",dob='1999-11-18',email='pavankum@gmail.com',gender='male',phoneno='8080808080',password='pavan@7979')
        patient_obj=patient.objects.get(id=p.id)
        d=doctor.objects.create(name="pavan",specalist="ENT",email="pavan@gmail.com",gender="male",phoneno="7981151302",password="Doctor@123",clinic_address="none")
        doctor_obj=doctor.objects.get(id=d.id)
        self.create_diagnostics=diagnostic.objects.create(patientId=patient_obj, doctorId=doctor_obj)
        diagnostic_obj=diagnostic.objects.get(id=self.create_diagnostics.id)
        self.assertTrue(isinstance(self.create_diagnostics, diagnostic))
        #add lab report
        self.create_lab_report=labreport.objects.create(diagnosticId=diagnostic_obj, lab_event='lab_event', lab_test_name='lab_test_name', lab_specimen_type='lab_specimen_type', lab_specimen_method='lab_specimen_method', lab_specimen_body_site='lab_specimen_body_site', lab_findings='lab_findings', lab_document='dianosis_image/teeth1.jpeg')
        self.assertTrue(isinstance(self.create_lab_report, labreport))
        #add Imaging Report
        self.create_imaging_report=imagingexam.objects.create(diagnosticId=diagnostic_obj,imaging_event='imaging_event', imaging_test_name='imaging_test_name', imaging_modality='imaging_modality', imaging_body_site='imaging_body_site', imaging_findings='imaging_findings', imaging_document='dianosis_image/teeth1.jpeg')
        self.assertTrue(isinstance(self.create_imaging_report, imagingexam))

