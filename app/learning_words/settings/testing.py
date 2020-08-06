from .dev import *
import tempfile

MEDIA_ROOT = tempfile.gettempdir()

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
  }
}