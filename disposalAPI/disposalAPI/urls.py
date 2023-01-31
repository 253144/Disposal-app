"""disposalAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Authentication.views import TokenCreateView, TokenRefreshView

from offer.views import ContainerViewSet, PriceViewSet
from clients.views import ClientViewSet, AddressViewSet
from orders.views import OrderViewSet, OrderListViewSet

router = routers.DefaultRouter()
router.register(r'list-of-orders', OrderListViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'Containers', ContainerViewSet)
router.register(r'prices', PriceViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Disposal API",
        default_version='v1',
        description="API for disposal container distributors",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Auth token requests
    path('token/create/', TokenCreateView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Root
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Django admin for database modification
    path('admin/', admin.site.urls),

    # Swagger urls
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
