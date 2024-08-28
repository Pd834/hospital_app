from django.urls import path
from .views import *

urlpatterns = [
    path('department/',DepartmentView.as_view()),
    path('patient/',PatientView.as_view()),
    path('doctor/',DoctorView.as_view()),
    path('patient/<int:id>/', PatientViewById.as_view()),
    path('doctor/<int:id>/', DoctorViewById.as_view()),
]