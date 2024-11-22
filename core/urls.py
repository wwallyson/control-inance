from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
 openapi.Info(
 title="Controle Financeiro API",
 default_version='v1',
 description="API para gerenciar receitas e despesas",
 ),
 public=True,
 permission_classes=(AllowAny,),
)

urlpatterns = [
 path('admin/', admin.site.urls),
 path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 path('api/', include('finance.urls')),

 path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
