from pathlib import Path
import os
 
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!lb^xhbl!-6l#d=kcc8mj6c&yx_(=@)e#iu!zdf#rf6-hy062w'
 
 
# Application definition
 
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'tasks',
   'users'
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
 
ROOT_URLCONF = 'todo.urls'
 
TEMPLATES = [
   {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [],
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
 
WSGI_APPLICATION = 'todo.wsgi.application'
 
 
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
 
TIME_ZONE = 'UTC'
 
USE_I18N = True
 
USE_L10N = True
 
USE_TZ = True
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
