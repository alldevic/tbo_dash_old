from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.schemas import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/schema.yaml', get_schema_view(
        title="TBO dashboard",
        version="1.0.0",
        permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    ), name='docs-schema'),
    path('auth/', include('djoser.urls.authtoken')),
]
