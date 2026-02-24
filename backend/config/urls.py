"""
URL configuration for Life OS 2026.

All API endpoints are versioned under /api/v1/.
Swagger/ReDoc documentation available in development.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# API v1 URL patterns
api_v1_patterns = [
    path("auth/", include("apps.users.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("goals/", include("apps.goals.urls")),
    path("calendar/", include("apps.calendar_app.urls")),
    path("journal/", include("apps.journal.urls")),
    path("gameplan/", include("apps.gameplan.urls")),
    path("learning/", include("apps.learning.urls")),
    path("finance/", include("apps.finance.urls")),
    path("health/", include("apps.health.urls")),
]

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # API v1
    path("api/v1/", include(api_v1_patterns)),
    # API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)