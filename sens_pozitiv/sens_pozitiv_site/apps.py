from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class sens_pozitivSiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sens_pozitiv_site"
    verbose_name = _("Site")
