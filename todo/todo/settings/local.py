from .base import *
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
 
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
 
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
 
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
 
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
 
