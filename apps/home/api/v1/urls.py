from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.home.api.v1.api import Home

app_name = "home"

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
