from django.views.generic import TemplateView
from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework import permissions


urlpatterns = [
    path('schema.yaml', get_schema_view(
        title="TBO dashboard",
        version="1.0.0",
        permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    ), name='docs_schema'),
    path('', TemplateView.as_view(template_name="index.html")),
]
