import os

from config.settings.base import BASE_DIR

DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'PORT': '5432',
        'HOST': 'localhost',
    }
}
SHARE_URL = "http://127.0.0.1:8000"  # Static assets
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)  # User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
