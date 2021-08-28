import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "session",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "WebServiceConsumers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",  # <-- social
                "social_django.context_processors.login_redirect",  # <-- social
            ],
        },
    },
]

LOGIN_URL = "login"
LOGOUT_URL = "logout"
LOGIN_REDIRECT_URL = "index"
SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/login"
LOGIN_ERROR_URL = "login"
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.yahoo.YahooOAuth2",
    "social_core.backends.linkedin.LinkedinOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

# Social
# -- GitHUB
SOCIAL_AUTH_GITHUB_KEY = os.getenv("ID_USER_GITHUB")
SOCIAL_AUTH_GITHUB_SECRET = os.getenv("SECRET_KEY_GITHUB")

# -- Facebook
# SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("ID_USER_FACEBOOK")
# SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("SECRET_KEY_FACEBOOK")
# SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", "user_link"]
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "id, name, email, picture.type(large), link"}
# SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
#     ("name", "name"),
#     ("email", "email"),
#     ("picture", "picture"),
#     ("link", "profile_url"),
# ]

# -- Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("ID_USER_GOOGLE")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("SECRET_KEY_GOOGLE")

# -- LinkedIn
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = os.getenv("ID_USER_LINKEDIN")
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = os.getenv("SECRET_KEY_LINKEDIN")


WSGI_APPLICATION = "DjangoAuth.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASES_NAME"),
        "USER": os.getenv("DATABASES_USER"),
        "PASSWORD": os.getenv("DATABASES_PASS"),
        "HOST": os.getenv("DATABASES_HOST"),
        "DATABASE_PORT": os.getenv("DATABASES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
