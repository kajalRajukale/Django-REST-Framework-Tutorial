from django.urls import include, path
from django.contrib import admin
from rest_framework.schemas import get_schema_view

API_TITLE = "Pastebin API"
API_DESCRIPTION = "A Web API for creating and viewing highlighted code snippets."

schema_view = get_schema_view(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version="1.0.0",
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("snippets.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("schema/", schema_view, name="openapi-schema"),
]
