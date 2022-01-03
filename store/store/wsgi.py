"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application

configuration = os.getenv('ENVIRONMENT', 'development').title()
os.environ.setdefault('DJANGO_CONFIGURATION', configuration)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

application = get_wsgi_application()
