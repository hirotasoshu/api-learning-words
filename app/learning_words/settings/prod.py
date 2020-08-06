import os
from .base import *

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = '/static_files/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media_files/'

SECRET_KEY = os.environ.get('SECRET_KEY')
API_SECRET = os.environ.get('API_SECRET')

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': "5432"
        }
}


## Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ALLOWED_HOSTS = [
    "127.0.0.1"
]

