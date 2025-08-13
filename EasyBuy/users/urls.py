from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RegisterUserView, UserRoleViewSet, UserProfileView,RoleViewSet

router = routers.DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'user-roles', UserRoleViewSet, basename='user-role')
urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenRefreshView.as_view(), name='token_logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]