from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.home.api.v1.api import HomeAPI

app_name = "home"

urlpatterns = [
    path('', HomeAPI.as_view(), name='home'),
]
