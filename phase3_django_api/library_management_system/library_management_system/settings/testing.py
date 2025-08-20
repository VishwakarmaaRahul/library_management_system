from .base import *  # import everything from base settings

print("⚡ Using TESTING environment with SQLite ⚡")

# -------------------------------------------------------------------
# Database
# -------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",   # Fast in-memory DB for tests
        "NAME": ":memory:",                       # Use in-memory DB
    }
}

# -------------------------------------------------------------------
# Installed apps
# -------------------------------------------------------------------
INSTALLED_APPS += [
    "library_management_system.libraries_database",  # your app
    # add other local apps here if you have them
]

# -------------------------------------------------------------------
# Other testing-specific overrides
# -------------------------------------------------------------------
DEBUG = False
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # faster tests
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
