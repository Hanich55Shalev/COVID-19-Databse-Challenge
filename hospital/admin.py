from django.contrib import admin
from .models import Hospital, Department, HospitalWorker, Patient, MedicalExaminationResult

admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(HospitalWorker)
admin.site.register(Patient)
admin.site.register(MedicalExaminationResult)
