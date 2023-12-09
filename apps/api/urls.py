from django.urls import path, include


urlpatterns = [
    path("user", include('apps.user.urls', "user")),
    path("product", include('apps.product.urls', "product")),
    path("cart", include('apps.cart.urls', "cart")),
]