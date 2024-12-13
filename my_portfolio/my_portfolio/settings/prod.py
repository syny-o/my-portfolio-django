from .base import *



DEBUG = False



ADMINS = [
    ('Syny', 'synek.o@seznam.cz'),
]


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
