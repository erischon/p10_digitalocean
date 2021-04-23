from . import *

SECRET_KEY = os.environ.get("SECRET_KEY", "password123")
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}