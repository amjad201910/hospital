from rest_framework import serializers
from django.db import transaction

from doctor.models import Doctor
from patient.models import Patient
from django.db.models import Max

from .models import Patient

from datetime import timedelta,datetime
from django.db.models import Q
from doctor.models import Doctor,Reservation
from hospitaladmin.models import Specialty



class ReservationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=60, source="Doctor.User.name", read_only=True)
    specialty = serializers.CharField(max_length=60, source="Doctor.specialty.Name", read_only=True)

    class Meta:
        model = Reservation
        fields = ['Doctor','Day','Time','username','specialty']
        extra_kwargs = {'Doctor': {'write_only': True}}

    def create(self, validated_data):
        validated_data['Doctor']=Doctor.objects.get(pk= self.context['view'].kwargs['pk'])

        if  validated_data['Doctor'].From>validated_data['Time']:
            raise serializers.ValidationError({"detail": "the Reservation is too early "})

        time_end=(datetime.combine(datetime.min, validated_data['Time']) + timedelta(hours=1)).time()

        if  validated_data['Doctor'].To<time_end:
            raise serializers.ValidationError({"detail": "the Reservation is too loang "})

        Reservations_times = Reservation.objects.values('Time').filter(
            Q(Doctor=validated_data['Doctor']) & Q(Day=validated_data['Day']))

        if Reservations_times.exists():


            for Reservation_time in Reservations_times :

                Reservation_time_end= (datetime.combine(datetime.min, Reservation_time['Time']) + timedelta(hours=1)).time()

                if (Reservation_time['Time']<= validated_data['Time'] <Reservation_time_end)or (Reservation_time['Time']<= time_end<Reservation_time_end) :
                    raise serializers.ValidationError({"detail": "the Reservation cut with other Reservation "})

        validated_data['Patient'] = self.context['request'].user.patient
        """

        time= Reservation.objects.filter(Q(pk=validated_data['Doctor'].pk)&Q(Day=validated_data['Day'])).aggregate(Max('Time'))['Time__max']
        print("////////////////////////////////////////////////////////////////////////")
        print(time)

        if time  is None:
           time= Doctor.objects.filter(pk=validated_data['Doctor'].pk).values('From').first()['From']
           print(time)
           print(type(time))
        time= (datetime.combine(datetime.min, time) + timedelta(hours=1)).time()
        print(time)
        validated_data['Time']=time
        validated_data['Patient']=self.context['request'].user.patient
        print(validated_data)
        """
        return super().create(validated_data)






class ShowSpecialtySerializer(serializers.ModelSerializer):
    Doctor=serializers.HyperlinkedIdentityField(view_name='showdoctor',lookup_field='pk',read_only=True)


    class Meta:
        model = Specialty
        fields = ['pk','Name','Doctor']







#############################################################
class ShowDoctorSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=60,source="User.name")
    Reservation=serializers.HyperlinkedIdentityField(view_name='addreservation',lookup_field='pk',read_only=True)


    class Meta:
        model = Doctor
        fields = ['pk','name','From','To','Reservation']











