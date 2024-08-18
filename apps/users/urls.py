from django.urls import path
from apps.users.views import RegisterUserAPIView, UsersAPIView, UserDetailAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("", UsersAPIView.as_view(), name="users"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-details"),

    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify-token"),
]