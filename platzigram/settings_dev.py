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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}