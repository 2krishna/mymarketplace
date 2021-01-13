from user.serializers import *
from rest_framework.decorators import action
from user.models import *
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

