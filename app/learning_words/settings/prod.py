import os
from .base import *

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = '/static_files/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media_files/'

SECRET_KEY = os.environ.get('SECRET_KEY', default='super-secret-key')
API_SECRET = os.environ.get('API_SECRET', default='md5-hash-doubletapp')

ALLOWED_HOSTS = [
    "127.0.0.1"
]

