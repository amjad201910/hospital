
from django.urls import path, include
from rest_framework import routers
from .views import UserCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'user', UserCreate, basename="user")

urlpatterns = [
  #  path('', UserCreate.as_view(), name="user"),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

       path('', include(router.urls)),

]
