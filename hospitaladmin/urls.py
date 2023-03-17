from django.urls import path,include
from rest_framework import routers
from .views import DoctorViewSet,PatientViewSet,SpecialtyViewSet







router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet, basename="doctor")
router.register(r'patient', PatientViewSet, basename="patient")
router.register(r'specialty', SpecialtyViewSet, basename="specialty")
urlpatterns = [
    path('', include(router.urls)),

]