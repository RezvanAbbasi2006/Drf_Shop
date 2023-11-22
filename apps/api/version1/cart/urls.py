from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.version1.cart.api import CartAPI

app_name = "cart"

urlpatterns = [
    path('cart/', CartAPI.as_view(), name='cart'),
]
