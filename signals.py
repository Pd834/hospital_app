from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import *

@receiver(post_save, sender=Patient)
def add_to_patient_group(sender,instance,created,**kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='Patients')
        instance.user.groups.add(group)

@receiver(post_save, sender=Doctor)
def add_to_doctor_group(sender,instance,created,**kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='Doctor')
        instance.user.groups.add(group)        

