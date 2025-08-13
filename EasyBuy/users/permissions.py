from rest_framework import permissions
from .models import UserRole

class HasRole(permissions.BasePermission):
    """
    Custom permission to only allow users with a specific role.
    """

    required_role = None

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        if not self.required_role:
            return False
        
        # Get the user's roles
        return UserRole.objects.filter(
            user=request.user,
            role__name=self.required_role).exists()

class IsAdminUser(HasRole):
    """
    Custom permission to only allow admin users.
    """
    required_role = 'Admin'

class IsBuyerUser(HasRole):
    """
    Custom permission to only allow buyer users.
    """
    required_role = 'Customer'

class IsSellerUser(HasRole):
    """
    Custom permission to only allow seller users.
    """
    required_role = 'Seller'