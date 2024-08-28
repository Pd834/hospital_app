from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class DepartmentView(APIView):
    def get(self, request):
        all_dept = Department.objects.all()
        dept_data = []
        for department in all_dept:
           single_dept ={
                "id":department.id,
                "name":department.name,
                "diagnostics":department.diagnostics,
                "location":department.location,
                "specialization":department.specialization
            }
        dept_data.append(single_dept)
        return Response(dept_data)

    def post(self,request):
        new_dept = Department(name=request.data["name"],diagnostics=request.data["diagnostics"],location=request.data["location"],specialization=request.data["specialization"])
        new_dept.save()
        return Response("Data Saved")
    
class PatientView(APIView):
    def get(self, request):
        all_patient = Patient.objects.all()
        patient_data = []
        for patient in all_patient:
           single_patient ={
                "id":patient.id,
                "record_id":patient.record_id,
                "patient_id":patient.patient_id,
                "create_date":patient.create_date,
                "diadnostics":patient.diadnostics,
                "observation":patient.observation,
                "treatment":patient.treatment,
                "user_id":patient.user_id,
                "department_id":patient.department_id
            }
        patient_data.append(single_patient)
        return Response(patient_data)
    def post(self,request):
        new_patient = Patient(record_id=request.data["record_id"],patient_id=request.data["patient_id"],create_Date=request.data["create_Date"],diadnostics=request.data["diadnostics"],observation=request.data["observation"],treatment=request.data["treatment"],user_id=request.data["user_id"],department_id=request.data["department_id"])
        new_patient.save()
        return Response("Data Saved")
class PatientViewById(APIView):
    def get(self,request,id):
        patient = Patient.objects.get(id = id)
        single_patient ={
                "id":patient.id,
                "record_id":patient.record_id,
                "patient_id":patient.patient_id,
                "create_date":patient.create_date,
                "diadnostics":patient.diadnostics,
                "observation":patient.observation,
                "treatment":patient.treatment,
                "user_id":patient.user_id,
                "department_id":patient.department_id
        }
        return Response(single_patient)

class DoctorView(APIView):
    def post(self,request):
        new_doctor = Doctor(user_id=request.data["user_id"],department_id=request.data["department_id"])
        new_doctor.save()
        return Response("Data Saved")
    
class DoctorViewById(APIView):
    def get(self,request,id):
        doctor = Doctor.objects.get(id = id)
        single_doctor ={
            "user_id":doctor.user_id,
            "department_id":doctor.department_id

        }
        return Response(single_doctor)
    def patch(self,request,id):
        patient = Patient.objects.filter(id=id)
        patient.update(record_id=request.data["record_id"],patient_id=request.data["patient_id"],create_Date=request.data["create_Date"],diadnostics=request.data["diadnostics"],observation=request.data["observation"],treatment=request.data["treatment"],user_id=request.data["user_id"],department_id=request.data["department_id"])
        return Response("updated")
    
    def delete(self,request,id):
        patient = Patient.objects.get(id = id)
        patient.delete()
        return Response("deleted")