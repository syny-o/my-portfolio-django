from .base import *



DEBUG = False



ADMINS = [
    ('Syny', 'synek.o@seznam.cz'),
]


ALLOWED_HOSTS = ['ondrejsynek.eu', 'www.ondrejsynek.eu']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
