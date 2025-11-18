import os

from django.core.wsgi import get_wsgi_application

# NOTE: Change 'myproject.settings' to your actual settings module path if different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'replenish.settings')

application = get_wsgi_application()