# library_management_system/settings/testing.py
from .base import *

DEBUG = True
SECRET_KEY = "test-secret-key"

# Use in-memory database for tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Faster password hashing during tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

ALLOWED_HOSTS = ["*"]
