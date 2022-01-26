from django.urls import path
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('roles/', roles, name='roles'),
    path('token/', get_token, name='get_token'),
    path('gender/', gender, name='gender'),
    path('doctor/', DoctorList.as_view(), name='doctor'),
    path('doctor/<int:pk>/', DoctorDetail.as_view()),
    path('patient/', PatientList.as_view(), name='patient'),
    path('patient/<int:pk>/', PatientDetail.as_view()),
]