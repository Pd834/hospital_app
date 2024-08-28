from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save

class Department(models.Model):
    name = models.CharField(max_length=200)
    diagnostics = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Patient(models.Model):
    record_id = models.IntegerField()
    patient_id = models.IntegerField()
    create_Date = models.DateField()
    diadnostics = models.CharField(max_length=200)
    observation = models.TextField()
    treatment = models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null =True)

    def __str__(self):
        return f"Patient:{self.user.username}"
        
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null =True)

    def __str__(self):
        return f"Doctor:{self.user.username}"
    
