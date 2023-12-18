from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path("home/", include("apps.home.urls", namespace='home')),
    path("user/", include("apps.user.urls", namespace='user')),
    path("product/", include("apps.product.urls", namespace='product')),
    path("cart/", include("apps.cart.urls", namespace='cart')),
]
