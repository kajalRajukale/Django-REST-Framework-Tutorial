from django.urls import include, path
from . import dashboard_views
from rest_framework.routers import DefaultRouter

from snippets import views

app_name = "snippets"

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', dashboard_views.home, name='home'),
    # Dashboard and CRUD views
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('dashboard/add/', dashboard_views.snippet_add, name='snippet_add'),
    path('dashboard/<int:pk>/edit/', dashboard_views.snippet_edit, name='snippet_edit'),
    path('dashboard/<int:pk>/delete/', dashboard_views.snippet_delete, name='snippet_delete'),
    path('dashboard/<int:pk>/preview/', dashboard_views.snippet_preview, name='snippet_preview'),
    # Profile page
    path('accounts/profile/', dashboard_views.profile, name='profile'),
    # API moved to /api/
    path('api/', include(router.urls)),
]
