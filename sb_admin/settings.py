"""
Django settings for sb_admin project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from pathlib import Path
import os
from urllib.parse import urlparse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'SECRET_KEY', default='37y@#ar4a$h+gzu^bq8xgh+=fvb-g&qh4z*hf2jqp%6o0j-%^0')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', default=False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_extensions',
    'crispy_forms',
    'accounts',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sb_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, os.path.join(BASE_DIR, 'templates'),
                 BASE_DIR, os.path.join(BASE_DIR, 'media')],
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

WSGI_APPLICATION = 'sb_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

parameters = {}

url = urlparse(
    os.getenv('DATABASE_URL', default='postgresql://user:user@localhost:5432/db'))

parameters['NAME'] = url.path[1:]

parameters['USER'] = url.netloc.split(':')[0]

parameters['PASSWORD'] = url.netloc.split(':')[1].split('@')[0]

parameters['HOST'] = url.netloc.split(':')[1].split('@')[1]

parameters['PORT'] = url.netloc.split(':')[2]

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': parameters['NAME'],

        'USER': parameters['USER'],

        'PASSWORD': parameters['PASSWORD'],

        'HOST': parameters['HOST'],

        'PORT': parameters['PORT'],

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

MAX_IMAGE_UPLOAD_SIZE = 5242880  # 5MB

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

GRAPPELLI_ADMIN_TITLE = 'SB Admin'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ORIGIN_WHITELIST = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://127.0.0.1:9000"
]

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://[a-zA-Z0-9\-]+\.herokuapp\.com$",
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
