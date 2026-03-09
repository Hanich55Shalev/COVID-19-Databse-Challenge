from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital)

    def __str__(self):
        return f'{self.hospital.name} - {self.name}'
