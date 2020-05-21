from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Адмнистрирование TBO Dashboard"
admin.site.site_title = "Адмнистрирование TBO Dashboard"
admin.site.index_title = "TBO Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', include('tbo_dash.docs.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('tbo_dash.dashboards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # Silk profiler
    urlpatterns = [
        path('silk/', include('silk.urls', namespace='silk')),
    ] + urlpatterns
