from .settings_common import *

from .dbsettings import db

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'parashabytes.zemon.name',
]

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db['database'],
        'USER': db['username'],
        'PASSWORD': db['password'],
        'HOST': db['hostname'],
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = 'https://parashastatic.zemon.name/'
STATIC_ROOT = '/var/www/vhosts/zemon.name/parashastatic.zemon.name'
