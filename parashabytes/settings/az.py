import sys

from .base import *
from .secrets import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += ['debug_toolbar']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if 'test' not in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': db['database'],
            'USER': db['username'],
            'PASSWORD': db['password'],
            'HOST': db['hostname'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_database',
        }
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
