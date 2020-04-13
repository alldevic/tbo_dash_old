from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/schema/', get_schema_view(
        title="TBO dashboard",
        version="1.0.0"
    ), name='docs-schema'),
    path('auth/', include('djoser.urls.authtoken')),
]
