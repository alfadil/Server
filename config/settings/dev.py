# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Add Django Debug Toolbar
"""

# pylint: disable=wildcard-import,unused-wildcard-import
from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DEBUG', default=True)

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env(
    'SECRET_KEY', default='!1%%f8qx!p8fjpvc!p%+np&07=ctxul7pxu@)fia6(i+4xo#k9')


# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar', 'django_extensions']


DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# In development, all tasks will be executed locally by blocking
# until the task returns
CELERY_ALWAYS_EAGER = True


# Interctive Shell for debugging
SHELL_PLUS = "bpython"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
