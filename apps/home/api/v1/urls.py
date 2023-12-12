from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.carts.api.v1.api import CartViewSet

app_name = "home"

router = DefaultRouter()
router.register('home', CartViewSet, basename='home')

urlpatterns = [
    path('api/', include(router.urls)),
]
