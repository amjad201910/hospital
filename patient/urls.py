from django.urls import path,include
from .views import AddReservation,ShowSpecialty,ShowDoctor

urlpatterns = [
    path('addreservation/<int:pk>/', AddReservation.as_view(), name="addreservation"),
    path('showspecialty/', ShowSpecialty.as_view(), name="showspecialty"),
    path('showdoctor/<int:pk>/', ShowDoctor.as_view(), name="showdoctor"),

]