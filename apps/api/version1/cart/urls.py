from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.version1.cart.api import CartViewSet

app_name = "cart"

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('api/', include(router.urls)),
]
