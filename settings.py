# settings.py
SECRET_KEY = 'your_secret_key'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
PASSWORD_HASHERS = [ 
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
