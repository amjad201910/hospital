
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.db import transaction
from core.serializers import creatuser



from core.serializers import UserSerializer

from patient.models import Patient
from doctor.models import Doctor
from .models import Specialty




class DoctorSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=60,source="User.username")
    name=serializers.CharField(max_length=60,source="User.name")
    personal_id=serializers.FileField(source="User.personal_id")
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Doctor
        fields = ['name','username','personal_id','password','License','certificate','specialty','url']
    @transaction.atomic()

    def create(self, validated_data):
        user=creatuser(validated_data)
        user.groups.set([3])
        validated_data['User'] = user

        return super().create(validated_data)







class PatientSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=60,source="User.username")
    name=serializers.CharField(max_length=60,source="User.name")
    personal_id=serializers.FileField(source="User.personal_id")
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Patient
        fields = ['name','username','personal_id','password','High','Weight','medical_history','url']
    @transaction.atomic()

    def create(self, validated_data):
        user=creatuser(validated_data)
        user.groups.set([4])
        validated_data['User'] = user

        return super().create(validated_data)






class  SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model=Specialty
        fields=['pk','Name','url']



