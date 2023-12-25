import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import environ
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9c4%pa+gw@hfk1^5ke*u7etn^vu1mu2vganw9((pcek38d$45f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

ALLOWED_HOSTS = ['*']

# Application definition
INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "apps.core",
    "apps.user",
    "apps.product",
    "apps.cart",
    "apps.home",
    "apps.api",
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    "django.contrib.humanize",
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",  # new
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = "user.User"
AUTHENTICATION_BACKENDS = [
    "apps.user.auth_backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gmarket',
        'USER': 'developer',
        'PASSWORD': '123456',
        'PORT': '5432',
        'HOST': 'localhost',
    }
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'ALLOWED_VERSION': ['v1'],
    'DEFAULT_VERSION': ['v1'],
    # 'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.IsAuthenticated'
    # ],
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CART_SESSION_ID = 'cart'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("fa", _("فارسی")),
    ("en", _("English")),
)

LOCALE_PATHS = [
    BASE_DIR / "locale/",
]

STATIC_URL = 'static/'

# env = environ.Env()
# environ.Env.read_env(BASE_DIR / ".env")


load_dotenv()
