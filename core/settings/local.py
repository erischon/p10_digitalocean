from . import *


SECRET_KEY = os.environ.get("SECRET_KEY", "password123")
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),) # for development

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'purbeurre', 
        'USER': 'postgres', 
        'PASSWORD': 'erischon2021',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}