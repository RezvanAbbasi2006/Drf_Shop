from django.urls import path

from apps.product.api.v1.api import ProductAPI, ProductCategoryAPI

app_name = 'product'

urlpatterns = [
    path('', ProductAPI.as_view(), name='product'),
    path('category/', ProductCategoryAPI.as_view(), name='category'),
]
