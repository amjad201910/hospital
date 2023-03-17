
from rest_framework.response import Response
from .models import User
from rest_framework import generics,viewsets
from .serializers import UserSerializer
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.parsers import FormParser,MultiPartParser



class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]