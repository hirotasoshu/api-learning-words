from .base import *

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "dev_db/db.sqlite3"),
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't3st'
API_SECRET = 't3st'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
