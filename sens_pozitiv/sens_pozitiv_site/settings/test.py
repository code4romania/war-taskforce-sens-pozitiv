from sens_pozitiv_site.settings.base import *

DEBUG = True
SECRET_KEY = "test_secret"
SITE_URL = "http://localhost"
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
