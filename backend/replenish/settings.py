import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('DJANGO_SECRET', 'dev-secret')
DEBUG = os.getenv('DEBUG', '1') == '1'
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend', 'dist')

ALLOWED_HOSTS = ['*',
    "replenish.onrender.com",
    "replenish-backend.onrender.com"
    'localhost',
    '127.0.0.1'
    ]    


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
    'rest_framework_simplejwt',
    ]


MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

ROOT_URLCONF = 'replenish.urls'


TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [FRONTEND_DIR],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
]

#STATIC FILES Configuration (For CSS/JS/Images) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Where 'collectstatic' will place files

# Tell Django where to look for static files *before* collection/serving
STATICFILES_DIRS = [
    # This folder contains your built CSS/JS/assets (usually inside 'dist')
    os.path.join(FRONTEND_DIR), 
]

WSGI_APPLICATION = 'replenish.wsgi.application'


# Use sqlite for quick start; update DATABASE_URL for production
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}


AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


MEDIA_URL = '/media/'



CORS_ALLOWED_ORIGINS = [
    "https://replenish.onrender.com",
]
CSRF_TRUSTED_ORIGINS = [
    "https://replenish.onrender.com",
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'