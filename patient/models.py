from django.db import models
from core.models import User
# Create your models here.

from core.models import upload_path
class Patient (models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    High=models.PositiveIntegerField()
    Weight=models.DecimalField( max_digits = 5,decimal_places = 2)
    medical_history=models.TextField()
