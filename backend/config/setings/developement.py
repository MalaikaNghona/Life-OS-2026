"""
Development settings for Life OS 2026.

Extends base settings with development-specific configuration.
Usage: DJANGO_SETTINGS_MODULE=config.settings.development
"""

from .base import *  # noqa: F401, F403

# =============================================================================
# DEBUG
# =============================================================================
DEBUG = True

# =============================================================================
# ALLOWED HOSTS
# =============================================================================
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# =============================================================================
# DATABASE — Override for SQLite fallback during early development
# =============================================================================
# Uncomment the block below if you don't have PostgreSQL set up yet:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# =============================================================================
# EMAIL — Console backend for development
# =============================================================================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# =============================================================================
# CORS — Allow all origins in development
# =============================================================================
CORS_ALLOW_ALL_ORIGINS = True

# =============================================================================
# CACHING — Local memory cache for development
# =============================================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "lifeos-dev-cache",
    }
}

# =============================================================================
# DRF — Browsable API available in development
# =============================================================================
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
)

# =============================================================================
# LOGGING — More verbose in development
# =============================================================================
LOGGING["root"]["level"] = "DEBUG"  # noqa: F405