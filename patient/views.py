from django.shortcuts import render
from .serializers import ReservationSerializer,ShowSpecialtySerializer,ShowDoctorSerializer

from rest_framework import generics,viewsets
from rest_framework.reverse import reverse
from rest_framework import status
from .models import  Patient
from hospitaladmin.models import Specialty
from doctor.models import Doctor,Reservation

class ShowDoctor(generics.ListAPIView):
    serializer_class = ShowDoctorSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        self.queryset = Doctor.objects.filter(specialty=pk)
        return super().get_queryset()
class ShowSpecialty(generics.ListAPIView):
    serializer_class = ShowSpecialtySerializer
    queryset = Specialty.objects.all()


class  AddReservation(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


"""
    def get_queryset(self):
        self.queryset = Reservation.objects.filter(Patient=self.request.user.patient)
        return super().get_queryset()
"""
