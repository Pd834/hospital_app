from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user','department')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user','department')

admin.site.register(Department)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
