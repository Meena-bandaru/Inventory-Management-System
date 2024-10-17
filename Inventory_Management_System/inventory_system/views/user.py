# inventory_item/views.py
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers.user import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

# Create a subclass of TokenObtainPairView for custom behavior if needed
class CustomTokenObtainPairView(TokenObtainPairView):
    # Optionally override methods to customize the response
    pass
