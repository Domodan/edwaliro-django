from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.serializers import *
from core.models import *

# Generic Class-based views

# Doctors list view
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(roles=self.request.role)

# Doctor details view
class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Patients list view
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Patient details view
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Index test page view
def index(request):
    return JsonResponse("Hello, welcome here!", safe=False)

# Login view
@api_view(['POST',])
def login(request):
    email = request.data['email']
    phone_number = request.data['phone_number']
    try:
        user = Doctor.objects.filter(email=email, phone_number=phone_number)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(user)
    return Response(status.HTTP_200_OK)

# Roles view
@api_view(['GET',])
def roles(request):
    roles = Roles.objects.all()
    serializers = RoleSerializer(roles, many=True)
    return Response(serializers.data)

# Gender view
@api_view(['GET',])
def gender(request):
    gender = Gender.objects.all()
    serializers = GenderSerializer(gender, many=True)
    return Response(serializers.data)

# Token Generator view
@api_view(['GET'])
def get_token(request):
    return Response({"token": "1234567890"})
