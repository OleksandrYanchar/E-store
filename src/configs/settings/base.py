import os
from pathlib import Path
import sys
from dotenv import load_dotenv

load_dotenv()

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_DIR = BASE_DIR.parent
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# APPS
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "store",
    "cart",
    "account",
    "payment",
]

THIRD_PARTY = [ 
               "mathfilters",
                "crispy_forms",]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS

# SECRET
SECRET_KEY = os.getenv("SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# MIDDLEWARES
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ACCOUNTS
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# TENPLATES

CRISPY_TEMPLATE_PACK = "bootstrap4"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# STATIC/MEDIA
STATIC_URL = "static/"

STATIC_ROOT = os.path.join(STATIC_DIR, "static/")

MEDIA_ROOT = os.path.join(STATIC_DIR, "media")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "static/media"


# OTHER
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"

STATIC_DIR = BASE_DIR.parent
WSGI_APPLICATION = "configs.wsgi.application"
ASGI_APPLICATION = "configs.asgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

ROOT_URLCONF = "configs.urls"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#OPTIONAL

#EMAIL

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "static/media"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "oleksandryancharr@gmail.com"
EMAIL_HOST_PASSWORD = "qcka julm linh rkny"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

