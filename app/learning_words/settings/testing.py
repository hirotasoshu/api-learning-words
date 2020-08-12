from .dev import *
import tempfile

MEDIA_ROOT = tempfile.gettempdir()

SECRET_KEY = 't3st'
API_SECRET = 't3st'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
  }
}