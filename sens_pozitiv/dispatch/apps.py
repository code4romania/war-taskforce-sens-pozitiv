from tabnanny import verbose

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DispatchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dispatch"
    verbose_name = _("Dispatch")
