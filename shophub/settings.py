"""
Django settings for the ShopHub project.

This file controls almost everything about how the project behaves:
which apps are installed, where the database lives, where templates
and static/media files are found, etc.
"""

from pathlib import Path

# BASE_DIR points to the root folder of the project (where manage.py lives).
# We use it to build all other paths, so the project works on any computer.
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------------
# SECURITY WARNING: keep this secret in real production use!
# For a learning project this is fine, but never share this key publicly
# for a real, live website.
# --------------------------------------------------------------------------
SECRET_KEY = 'django-insecure-shophub-demo-key-change-this-in-production'

# DEBUG = True shows detailed error pages. Turn this OFF (False) in production.
# shophub/settings.py

DEBUG = False  # Or True, depending on your needs

# Add your local addresses here:
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# --------------------------------------------------------------------------
# Installed Apps
# Every Django "app" is a self-contained feature module. We list Django's
# built-in apps first, then our own custom apps below.
# --------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # Needed for session-based cart & login
    'django.contrib.messages',   # Needed for "flash" style success/error messages
    'django.contrib.staticfiles',

    # Our custom apps
    'accounts',
    'products',
    'cart',
    'wishlist',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shophub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # We keep ONE shared "templates" folder at the project root
        # (instead of scattering templates inside each app) — this is
        # simpler for beginners to navigate.
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom context processor: makes the cart item count and
                # cart total available in EVERY template (e.g. navbar badge).
                'cart.context_processors.cart_summary',
            ],
        },
    },
]

WSGI_APPLICATION = 'shophub.wsgi.application'


# --------------------------------------------------------------------------
# Database
# SQLite is a simple file-based database — perfect for learning & small
# projects. Django creates the db.sqlite3 file automatically.
# --------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --------------------------------------------------------------------------
# Password validation
# --------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --------------------------------------------------------------------------
# Internationalization
# --------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --------------------------------------------------------------------------
# Static files (CSS, JavaScript, images that are part of the site design)
# --------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # Where we keep our source CSS/JS during development
STATIC_ROOT = BASE_DIR / 'staticfiles'     # Where `collectstatic` gathers files for production

# --------------------------------------------------------------------------
# Media files (content uploaded by users/admin, e.g. product photos)
# --------------------------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------------------------
# Auth redirects
# Tell Django where to send users after login/logout, and where the login
# page lives, so we can use the @login_required decorator everywhere.
# --------------------------------------------------------------------------
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
DEBUG = False

ALLOWED_HOSTS = [
    "your-domain.com",
    "your-app.onrender.com",
]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]