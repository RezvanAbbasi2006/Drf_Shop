from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.api.v1.api import RegisterAPIView, EmailTokenObtainPairView, LoginApiView, ResetPasswordApi, \
    ConfirmPasswordApi

app_name = "user"

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('reset_password/', ResetPasswordApi.as_view(), name='reset_password'),
    path('confirm_password/', ConfirmPasswordApi.as_view(), name='confirm_password'),
    path('token/obtain/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
