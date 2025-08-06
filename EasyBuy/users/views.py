from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterUserSerializer
from .models import User
# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        # Optionally, you can send a welcome email or perform other actions here
        # For example: send_welcome_email(user)
        return user