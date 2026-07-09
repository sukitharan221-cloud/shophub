"""ASGI config for shophub project. Used for async deployments."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shophub.settings')
application = get_asgi_application()
