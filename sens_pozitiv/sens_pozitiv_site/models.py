from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

EMAIL_TEMPLATE_CHOICES = [
    ("patient_request", _("Patient Request Form")),
]


class EmailTemplate(models.Model):
    template = models.CharField(_("Template"), choices=EMAIL_TEMPLATE_CHOICES, max_length=50)
    text_content = models.TextField(_("Text content"))
    html_content = RichTextField(_("HTML content"), blank=True)
    lang = models.CharField(_("Language"), choices=settings.LANGUAGES, max_length=2)

    class Meta:
        verbose_name = _("Email template")
        verbose_name_plural = _("Email templates")
        unique_together = ["template", "lang"]

    def __str__(self):
        return f"{self.get_template_display()} ({self.get_lang_display()})"
