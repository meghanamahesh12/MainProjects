from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def _str_(self):
        return self.Name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Appoinment(models.Model):
    doctor = models.CharField(max_length=50)
    patient = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    
    
