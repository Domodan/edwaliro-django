from django.db import models
from django.db.models.fields.related import RelatedField
# from django.db.models import fields
# from django.forms import ModelForm

GENDER = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
]

##########  Models  #########

# Roles model
class Roles(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Gender models
class Gender(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender

# Doctor model.
class Doctor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


# Patient model
class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nin = models.CharField(max_length=100)
    weight = models.CharField(max_length=100, default=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


# ######## Forms Models #########

# # Doctor Form Model
# class DoctorForm(ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'

# # Patient Form Model
# class PatientForm(ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'
