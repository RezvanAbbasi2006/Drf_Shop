from django.urls import path

from apps.product.api.v1.api import ProductAPI

app_name = 'product'

urlpatterns = [
    path('', ProductAPI.as_view(), name='product'),
]
