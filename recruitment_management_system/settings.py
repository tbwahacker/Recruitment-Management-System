"""
Django settings for recruitment_management_system project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jl+t198i+^_56hf#i70_dx-mihh!j6gk!9&uvr8@sr6-ggp0)g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['62.169.25.50']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Apps
    'job_portal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recruitment_management_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'recruitment_management_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py

LOGOUT_REDIRECT_URL = '/logout'  # Change this to a URL that exists in your project

MEDIA_ROOT = os.path.join(BASE_DIR, 'resumes')
MEDIA_URL = '/resumes/'

# AZAM PAY INTEGRATION
APP_NAME = 'UzaNasi'
CLIENT_ID = 'a3186091-45e4-4a99-887c-06492fcbce41'
CLIENT_SECRET = 'SkHFXFU3gXscHAiSxfpWDRITBN3TTPgY9dYqyMvqtyAEJY85iO+ez5LWxcaUSoCcNDMKJ3EgNBBiDIRY1ExOhVIok/6Kevd5b59ewBjQqK1HrENemORTYsAnUyiBsxBxhW/rZabFGehLpJwMbmHQ+jTxlCK5LK9BmI3OiT0C1TdR3N3TRsot+edxZq3okBb8AJnaissZIdUff92UnbBzRc8HTbnPuOO5ZYd/FWG2Foer38o4c3Lm1uBG8VwkcVTQpAowieSL4QQefYB9MbG0KWkEEW2xAnVvOJ1h9uh8RVvfZgqT/WlF8RTn0GGBB6tz0TuZJtg3bjuFl9XEaJgW1F4de2Q54cdB/ringX2KqJ+Mk5TMIs854tS82+ANCjY/xGhCMAVZpEFSt4bFiH1A1okgdwbQSTOvuiFaGXL5L5J6geBj4WcgvRU6bdlhI7fy/Vhn/O4Ay946w/iH/zkLyie/R12Ai8OSnhY1si8CIxhJhMguCdN24XD5NEHcfhCAk29nJBQlgNDJPQwKgU4gsWJQwgzU4qYxHodaOtP/7Eb3XZwK7SdLz2mcqL5b75EpFni0irx8tAF49I+jfPy1Vq3DBCnRh0VsrpZCkkgFdU0/t/ull7gPPcWRHBPRnpJR/YBFYTlUShpROFsZ1D791YFcWI5WW2bqaLIFKdnl9g0='
X_API_KEY = '5200399e-389e-4d27-b48d-09b4d1c86ae6'