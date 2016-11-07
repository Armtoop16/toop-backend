# Django settings for app project.

# Stdlib imports
import os
import sys

# Third-party app imports
import cloudinary

SYSTEM_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set environment

ENV = os.environ.get('APP_ENVIRONMENT', None)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('APP_SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if ENV == 'prod' else True

ALLOWED_HOSTS = [os.environ.get('APP_ALLOWED_HOSTS', '')]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',

    'rest_auth',
    'rest_auth.registration',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'push_notifications',

    'apps.cli',
    'apps.core.accounts',
    'apps.core.images',
    'apps.web.home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'accounts.User'

WSGI_APPLICATION = 'system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('APP_DB_PGSQL_DATABASE', None),
        'USER': os.environ.get('APP_DB_PGSQL_USERNAME', None),
        'PASSWORD': os.environ.get('APP_DB_PGSQL_PASSWORD', None),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

MEDIA_URL = '/media/'

# Email Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sparkpostmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'SMTP_Injection'
EMAIL_HOST_PASSWORD = os.environ.get('APP_EMAIL_API_KEY', None)
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'django-sparkpost@sparkpostbox.com'

# Sites

SITE_ID = 1

# Django AllAuth

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_EMAIL_VERIFICATION = None
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': [
            'email',
            'user_friends',
            'public_profile',
            'user_birthday',
            'user_likes'
        ],
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
            'birthday',
            'picture',
        ],
    }
}

# Django Rest Swagger

SWAGGER_SETTINGS = {
    'is_authenticated': True,
    'is_superuser': True,
}

# Cloudinary

cloudinary.config(
    cloud_name=os.environ.get("APP_CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("APP_CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("APP_CLOUDINARY_API_SECRET")
)
