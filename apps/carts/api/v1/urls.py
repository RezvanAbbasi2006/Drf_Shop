from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.carts.api.v1.api import CartViewSet

app_name = "carts"

router = DefaultRouter()
router.register('carts', CartViewSet, basename='carts')

urlpatterns = [
    path('api/', include(router.urls)),
]
