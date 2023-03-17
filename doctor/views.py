from .models import Doctor,Reservation,Prescription
from rest_framework import generics,viewsets
from .serializers import ShowReservationSerializer,PrescriptionSerializer
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.parsers import FormParser,MultiPartParser

from rest_framework import status
from rest_framework.response import Response
from patient.models import Patient
class ShowReservation(generics.ListAPIView):
    serializer_class = ShowReservationSerializer

    def get_queryset(self):
        self.queryset = Reservation.objects.filter(Doctor=self.request.user.doctor)
        return super().get_queryset()

class PrescriptionListCreate(generics.ListCreateAPIView):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()
    def get_queryset(self):
        pk = self.kwargs['pk']
        reservation= Reservation.objects.get(pk=pk)

        self.queryset = Prescription.objects.filter(Reservation__Patient=reservation.Patient)
        return super().get_queryset()



    def get(self, request, *args, **kwargs):
        data= super().get(request,*args, **kwargs).data
        pk = kwargs['pk']
       # reservation = Reservation.objects.get(pk=pk)
        user=Patient.objects.get(reservation__pk=pk)
        response={
            'medical_history': user.medical_history,
            'Weight': user.Weight,
            'High': user.High,
            'Prescriptions': data,


        }

        # response.insert(0,{'medical_history':user.medical_history})
        # response.insert(1,{'Weight':user.Weight})
        # response.insert(1,{'High':user.High})
        return Response(response)


