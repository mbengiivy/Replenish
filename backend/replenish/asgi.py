import os

from django.core.asgi import get_asgi_application

# NOTE: Change 'myproject.settings' to your actual settings module path if different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'replenish.settings')

application = get_asgi_application()