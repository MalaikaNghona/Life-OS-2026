"""
Production settings for Life OS 2026.

Extends base settings with production-specific security and performance
configuration.
Usage: DJANGO_SETTINGS_MODULE=config.settings.production
"""

from .base import *  # noqa: F401, F403

# =============================================================================
# DEBUG — Never True in production
# =============================================================================
DEBUG = False

# =============================================================================
# SECURITY
# =============================================================================
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# =============================================================================
# CORS — Strict in production
# =============================================================================
CORS_ALLOW_ALL_ORIGINS = False

# =============================================================================
# CACHING — Redis in production
# =============================================================================
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL", default="redis://127.0.0.1:6379/1"),  # noqa: F405
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# =============================================================================
# DRF — JSON only in production
# =============================================================================
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
)

# =============================================================================
# LOGGING — File-based in production
# =============================================================================
LOGGING["root"]["handlers"] = ["console", "file"]  # noqa: F405
LOGGING["root"]["level"] = "WARNING"  # noqa: F405