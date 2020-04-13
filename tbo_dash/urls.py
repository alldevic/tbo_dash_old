from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/schema/', get_schema_view(
        title="TBO dashboard",
        description="API for all things …",
        version="1.0.0"
    ), name='docs-schema'),
    path('auth/', obtain_auth_token, name='auth'),
]
