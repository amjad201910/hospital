from django.contrib import admin

from .models import Doctor, Reservation, Prescription, Prescription_Image, Prescription_Image_File


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'User',
        'License',
        'certificate',
        'specialty',
        'From',
        'To',
    )
    list_filter = ('User', 'specialty')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'Doctor', 'Patient', 'Day', 'Time')
    list_filter = ('Doctor', 'Patient', 'Day')


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Reservation', 'Body')
    list_filter = ('Reservation',)


@admin.register(Prescription_Image)
class Prescription_ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Image', 'Prescription')
    list_filter = ('Prescription',)


@admin.register(Prescription_Image_File)
class Prescription_Image_FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'Image_File', 'Prescription')
    list_filter = ('Prescription',)
