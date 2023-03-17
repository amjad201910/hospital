from django.db import models
from core.models import User
# Create your models here.
from core.models import upload_path
from hospitaladmin.models import Specialty
from patient.models import Patient
from core.models import upload_path

class Doctor (models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    License=models.FileField(upload_to=upload_path, blank=True, null=True)
    certificate=models.FileField(upload_to=upload_path, blank=True, null=True)
    specialty=models.ForeignKey(Specialty,on_delete=models.CASCADE)

    From = models.TimeField()
    To = models.TimeField()








class Reservation(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Day=models.DateField()
    Time = models.TimeField()


class Prescription(models.Model):
    Reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    Body=models.TextField(blank=True, null=True)


class Prescription_Image(models.Model):
    Image=models.ImageField(upload_to=upload_path, blank=True, null=True)

    Prescription= models.ForeignKey(Prescription, on_delete=models.CASCADE)

class Prescription_Image_File(models.Model):
    Image_File=models.FileField(upload_to=upload_path, blank=True, null=True)


    Prescription= models.ForeignKey(Prescription, on_delete=models.CASCADE)

