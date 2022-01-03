"""
ASGI config for store project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application # noqa

configuration = os.getenv('ENVIRONMENT', 'development').title()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', configuration)

from configurations import importer  # noqa
importer.install()

application = get_asgi_application()
