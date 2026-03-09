from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hospital.name} - {self.name}'
    
class HospitalWorker(models.Model):
    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', 'Female'),
        ('O', 'Other')
    )

    POSITION_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse')
    )

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    positon = models.CharField(max_length=10, choices=POSITION_CHOICES)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return f'{self.positon} {self.name}'
    
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', 'Female'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class MedicalExaminationResult(models.Model):
    EXAMINATION_RESULTS = (
        ('healthy', 'Healthy'),
        ('corona', 'Corona'),
        ('botism', 'Botism'),
        ('dead', 'Dead')
    )
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    performer = models.ForeignKey(HospitalWorker, on_delete=models.CASCADE)
    time = models.DateTimeField()
    result = models.CharField(max_length=10, choices=EXAMINATION_RESULTS)
