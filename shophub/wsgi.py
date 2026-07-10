"""WSGI config for shophub project. Used when deploying to a real server."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shophub.settings')
application = get_wsgi_application()
