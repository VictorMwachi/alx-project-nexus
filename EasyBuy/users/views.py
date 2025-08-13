from rest_framework import generics, permissions,viewsets
from .serializers import RegisterUserSerializer, RoleSerializer, UserRoleSerializer, UserProfileSerializer
from .models import User, Role, UserRole, UserProfile


# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        # Optionally, you can send a welcome email or perform other actions here
        # For example: send_welcome_email(user)
        return user

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user.id)

    def perform_update(self, serializer):
        user = serializer.save()
        # Optionally, you can send a notification or perform other actions here
        # For example: send_profile_update_notification(user)
        return user

class RoleViewSet(viewsets.ModelViewSet):
    """A viewset for managing user roles."""
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Role.objects.all()
    
class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserRole.objects.filter(user=self.request.user)