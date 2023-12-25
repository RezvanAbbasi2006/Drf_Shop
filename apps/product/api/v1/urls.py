from django.urls import path

from apps.product.api.v1.api import ProductViewSet, ProductCategoryAPI

app_name = 'product'

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product'),
    path('category/', ProductCategoryAPI.as_view(), name='category'),
]
