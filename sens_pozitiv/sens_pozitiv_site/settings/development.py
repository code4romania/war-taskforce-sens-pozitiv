from sens_pozitiv_site.settings.base import *

DEBUG = True
ENABLE_DEBUG_TOOLBAR = env("ENABLE_DEBUG_TOOLBAR", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CORS_ORIGIN_ALLOW_ALL = True
SECRET_KEY = "secret"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django_q_email.backends.DjangoQBackend"

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
] + INSTALLED_APPS

INSTALLED_APPS.append("django_extensions")

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

    def show_toolbar(_):
        return True

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
