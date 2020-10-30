"""Settings for dev enviroment."""

# Django
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""Debug mode turned on."""
DEBUG = True

"""Localhost."""
ALLOWED_HOSTS = []


"""Local database SQLite."""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5433',
        'USER': 'matteo',
        'PASSWORD': '',
        'NAME': 'platzi',
        'CHARSET': 'utf8',
    }
}