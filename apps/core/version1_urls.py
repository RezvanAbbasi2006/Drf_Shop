from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("product/", include("apps.api.version1.product.urls", namespace="product")),
    path("cart/", include("apps.api.version1.cart.urls", namespace="cart")),
    path('user/', include('apps.api.version1.user.urls', namespace="user")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
