from rest_framework.routers import SimpleRouter

from django.conf.urls.static import static
from django.conf import settings

from product.views import ProductViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)

from django.contrib import admin
from django.urls import path, include, re_path

from cart.views import CartApiView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# TODO Category ViewSet -> Admin

schema_view = get_schema_view(
    openapi.Info(
        title="Shop_market API",
        default_version='v1',
        description="ev.22 Shop marker rest proj",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/cart/', CartApiView.as_view()),
    path('api/v1/orders/', include('order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
