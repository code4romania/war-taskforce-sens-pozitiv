from sens_pozitiv_site.settings.base import *

DEBUG = False

SECRET_KEY = env.str("SECRET_KEY")

EMAIL_BACKEND = "django_q_email.backends.DjangoQBackend"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
