"""
Django settings for sens_pozitiv_site project.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from os import path

import environ
from django.utils.translation import gettext_lazy as _

env = environ.Env(
    # set casting, default value
    ENVIRONMENT=(str, "production"),
    DEBUG=(str, "no"),
    ENABLE_DEBUG_TOOLBAR=(str, "no"),
    LANGUAGE_CODE=(str, "en"),
    HOME_SITE_URL=(str, ""),
    ALLOWED_HOSTS=(list, ["*"]),
    SLACK_WEBHOOK_URL=(str, ""),
    SLACK_LOGGING_COLOR=(str, ""),
    ENABLE_SLACK_LOGGING=(str, "no"),
    RECAPTCHA_PUBLIC_KEY=(str, ""),
    RECAPTCHA_PRIVATE_KEY=(str, ""),
    FROM_EMAIL=(str, "webmaster@localhost"),
)

ADMIN_TITLE = _("Positive Sense Dispatcher")
ADMIN_TITLE_SHORT = _("PSD")

LIST_PER_PAGE = 10

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.join(path.dirname(path.abspath(__file__)), "../..")

DEBUG = env("DEBUG") == "yes"
ENVIRONMENT = env("ENVIRONMENT")
ENABLE_DEBUG_TOOLBAR = DEBUG and (env("ENABLE_DEBUG_TOOLBAR")) == "yes"

SLACK_WEBHOOK_URL = env("SLACK_WEBHOOK_URL")
SLACK_LOGGING_COLOR = env("SLACK_LOGGING_COLOR")
ENABLE_SLACK_LOGGING = env("ENABLE_SLACK_LOGGING") == "yes"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CORS_ORIGIN_ALLOW_ALL = False

INSTALLED_APPS = [
    "jazzmin",
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    "django.contrib.postgres",
    # third-party apps
    "storages",
    "import_export",
    "multiselectfield",
    "django_q",
    "crispy_forms",
    "captcha",
    "ckeditor",
    # "django_plotly_dash.apps.DjangoPlotlyDashConfig",
    "phonenumber_field",
    # project apps
    "static_custom",
    "app_account",
    "dispatch",
    "sens_pozitiv_site",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django_plotly_dash.middleware.BaseMiddleware",
    # "django_plotly_dash.middleware.ExternalRedirectionMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SITE_ID = 1

ROOT_URLCONF = "sens_pozitiv_site.urls"

X_FRAME_OPTIONS = "SAMEORIGIN"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [path.join(BASE_DIR, "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "sens_pozitiv_site.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = env("LANGUAGE_CODE")
TIME_ZONE = "Europe/Bucharest"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ("ro", _("Romanian")),
    ("en", _("English")),
    ("uk", _("Ukrainian")),
    ("ru", _("Russian")),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

PRIVATE_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_URL = "/media/"
MEDIA_ROOT = path.join(BASE_DIR, "./public/media")

STATIC_URL = "/static/"
STATIC_ROOT = path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # "django_plotly_dash.finders.DashAssetFinder",
    # "django_plotly_dash.finders.DashComponentFinder",
    # "django_plotly_dash.finders.DashAppDirectoryFinder",
]

LOCALE_PATHS = (path.join(BASE_DIR, "locale"),)

# PLOTLY_DASH = {
#     "view_decorator": "django_plotly_dash.access.login_required",
# }

# PLOTLY_COMPONENTS = [
#     # Common components
#     "dash_core_components",
#     "dash_html_components",
#     "dash_renderer",
#     # django-plotly-dash components
#     "dpd_components",
#     # static support if serving local assets
#     "dpd_static_support",
#     # Other components, as needed
#     "dash_bootstrap_components",
# ]

# MEMCACHED_HOST = env("MEMCACHED_HOST")
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": MEMCACHED_HOST,
#     },
# }

COUNTIES_SHORTNAME = {
    "AB": "Alba",
    "AR": "Arad",
    "AG": "Argeș",
    "BC": "Bacău",
    "BH": "Bihor",
    "BN": "Bistrița-Năsăud",
    "BT": "Botoșani",
    "BV": "Brașov",
    "BR": "Brăila",
    "B": "București",
    "BZ": "Buzău",
    "CL": "Călărași",
    "CS": "Caraș-Severin",
    "CJ": "Cluj",
    "CT": "Constanța",
    "CV": "Covasna",
    "DB": "Dâmbovița",
    "DJ": "Dolj",
    "GL": "Galați",
    "GR": "Giurgiu",
    "GJ": "Gorj",
    "HR": "Harghita",
    "HD": "Hunedoara",
    "IL": "Ialomița",
    "IS": "Iași",
    "IF": "Ilfov",
    "MM": "Maramureș",
    "MH": "Mehedinți",
    "MS": "Mureș",
    "NT": "Neamț",
    "OT": "Olt",
    "PH": "Prahova",
    "SM": "Satu Mare",
    "SJ": "Sălaj",
    "SB": "Sibiu",
    "SV": "Suceava",
    "TR": "Teleorman",
    "TM": "Timiș",
    "TL": "Tulcea",
    "VS": "Vaslui",
    "VL": "Vâlcea",
    "VN": "Vrancea",
}

COUNTY_CHOICES = list(COUNTIES_SHORTNAME.items())

AUTH_USER_MODEL = "app_account.CustomUser"
# LOGIN_REDIRECT_URL = "admin"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

IMPORT_EXPORT_USE_TRANSACTIONS = True

EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS") == "yes"
EMAIL_USE_SSL = env("EMAIL_USE_SSL") == "yes"
FROM_EMAIL = env("FROM_EMAIL")

SUPER_ADMIN_PASS = env("SUPER_ADMIN_PASS")
SUPER_ADMIN_EMAIL = env("SUPER_ADMIN_EMAIL")
SUPER_ADMIN_FIRST_NAME = env("SUPER_ADMIN_FIRST_NAME")
SUPER_ADMIN_LAST_NAME = env("SUPER_ADMIN_LAST_NAME")

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": [
            ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
            [
                "NumberedList",
                "BulletedList",
                "Indent",
                "Outdent",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"],
            ["Undo", "Redo"],
            ["Source"],
            ["Maximize"],
        ],
        "height": 400,
        "width": "100%",
    },
}
CKEDITOR_BASEPATH = f"{STATIC_URL}ckeditor/ckeditor/"

# django-q https://django-q.readthedocs.io/en/latest/configure.html

Q_CLUSTER = {
    "name": "SdU",
    "recycle": 500,
    "timeout": 60,
    "compress": True,
    "save_limit": 250,
    "queue_limit": 500,
    "cpu_affinity": 1,
    "label": "Django Q",
    "orm": "default",
}

# django-jazzmin
# -------------------------------------------------------------------------------
# django-jazzmin - https://django-jazzmin.readthedocs.io/configuration/

JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": ADMIN_TITLE,
    # Title on the brand, and the login screen (19 chars max)
    "site_header": ADMIN_TITLE,
    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": "jazzmin/img/commitglobal.svg",
    "site_icon": "jazzmin/img/sprijin-de-urgenta-logo.svg",
    "site_logo_classes": "site-logo",
    # Welcome text on the login screen
    "welcome_sign": ADMIN_TITLE,
    # Copyright on the footer
    "copyright": "Commit Global - War Task Force",
    # The model admin to search from the search bar, search bar omitted if excluded
    # "search_model": "donors.Donor",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": _("Home"), "url": "admin:index", "permissions": ["auth.view_user"]},
        {
            "name": _("External Form"),
            "url": "patient_request_form",
            "permissions": ["auth.view_user"],
            "new_window": True,
        },
        {"name": _("A Commit Global solution. Find Out More"), "url": "https://www.commitglobal.org/", "new_window": True},
        # external url that opens in a new window (Permissions can be added)
        # {
        #     "name": "View website",
        #     "url": "https://github.com/farridav/django-jazzmin/issues",
        #     "new_window": True,
        # },
        # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {
        #     "name": "Support",
        #     "url": "https://github.com/farridav/django-jazzmin/issues",
        #     "new_window": True,
        # },
        {"model": "auth.user"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # "hide_apps": ['django_plotly_dash',],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        # "books": [
        #     {
        #         "name": "Make Messages",
        #         "url": "make_messages",
        #         "icon": "fas fa-comments",
        #         "permissions": ["books.view_book"],
        #     }
        # ]
    },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "account.EmailAddress": "fas fa-at",
        "django_q.Failure": "fas fa-times",
        "django_q.Schedule": "fas fa-calendar-check",
        "django_q.Success": "fas fa-check",
        #
        "app_account.CustomUser": "fas fa-user",
        "dispatch.Clinic": "fas fa-hospital",
        "dispatch.PatientRequest": "fas fa-hospital-user",
        "sens_pozitiv_site.EmailTemplate": "fas fa-at",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "jazzmin/css/admin.css",
    "custom_js": "jazzmin/js/admin.js",
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": bool(ENVIRONMENT != "production"),
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cosmo",
    "dark_mode_theme": None,
}

# Recaptcha settings
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY", default="")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY", default="")

if not RECAPTCHA_PUBLIC_KEY:
    SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

CRISPY_TEMPLATE_PACK = "bootstrap4"

NOTIFICATIONS_EMAIL = env("NOTIFICATIONS_EMAIL", default="")
NOTIFICATIONS_REPLYTO_EMAIL = env("NOTIFICATIONS_REPLYTO_EMAIL", default="")
NOTIFICATIONS_X_SES_CONFIGURATION_SET_HEADER = env("NOTIFICATIONS_X_SES_CONFIGURATION_SET_HEADER", default="")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "slack": {
            "level": "ERROR",
            "class": "sens_pozitiv_site.handlers.SlackHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["slack", "console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

ADMINS = (("Slack Error Logging", "not_a_real_email@code4.ro"),)
