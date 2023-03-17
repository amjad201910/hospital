
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64ImageField

from core.serializers import UserSerializer
from .models import Doctor,Reservation,Prescription,Prescription_Image,Prescription_Image_File


class ShowReservationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, source="Patient.User.name", read_only=True)
    prescription=serializers.HyperlinkedIdentityField(view_name='prescription',lookup_field='pk',read_only=True)

    class Meta:
        model = Reservation
        fields = ['pk','Day','Time','name','prescription']




class ImageSerializer(serializers.ModelSerializer):
    Image=Base64ImageField()
    class Meta:
        model = Prescription_Image
        fields = ['pk','Image']


class Image_FileSerializer(serializers.ModelSerializer):
    Image_File=Base64ImageField()
    class Meta:
        model = Prescription_Image_File
        fields = ['pk','Image_File']





class PrescriptionSerializer(serializers.ModelSerializer):
    Image_Files=Image_FileSerializer(source='prescription_image_file_set',many=True)
    Images=ImageSerializer(source='prescription_image_set',many=True)
    Day=serializers.DateField(source='Reservation.Day',read_only=True)
    specialty=serializers.CharField(source='Reservation.Doctor.specialty.Name',read_only=True)
    doctor=serializers.CharField(source='Reservation.Doctor.User.name',read_only=True)
    class Meta:
        model = Prescription
        fields = ['pk','Body','Day','specialty','doctor','Image_Files','Images']

    def create(self, validated_data):

            validated_data['Reservation']=Reservation.objects.get(pk= self.context['view'].kwargs['pk'])
            Image_Files=validated_data.pop('Image_Files')
            Images=validated_data.pop('Images')

            prescription= super().create(validated_data)

            Images_Files_Serializer=Image_FileSerializer(data=Image_Files,many=True)
            Images_Files_Serializer.is_valid(raise_exception=True)
            Images_Files_Serializer.save(Prescription=prescription)



            Images_Serializer=ImageSerializer(data=Images,many=True)
            Images_Serializer.is_valid(raise_exception=True)
            Images_Serializer.save(Prescription=prescription)

            return prescription

