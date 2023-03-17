from django.contrib import admin

from .models import Patient



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'High', 'Weight', 'medical_history')
    list_filter = ('User',)
