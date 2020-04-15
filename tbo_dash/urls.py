from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Адмнистрирование TBO Dashboard"
admin.site.site_title = "Адмнистрирование TBO Dashboard"
admin.site.index_title = "TBO Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include('tbo_dash.docs.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # Silk profiler
    urlpatterns = [
        path('silk/', include('silk.urls', namespace='silk')),
    ] + urlpatterns
