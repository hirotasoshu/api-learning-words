import os
from .base import *

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = '/static_files/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media_files/'

SECRET_KEY = os.environ.get('SECRET_KEY', default='super-secret-key')
API_SECRET = os.environ.get('API_SECRET', default='md5-hash-doubletapp')

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

