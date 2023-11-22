from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.version1.product.api import ProductAPI

app_name = "product"

urlpatterns = [
    path('product/', ProductAPI.as_view(), name='product'),
]
