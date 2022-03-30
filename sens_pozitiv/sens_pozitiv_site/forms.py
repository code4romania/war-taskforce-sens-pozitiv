from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from dispatch.models import PatientRequest


class PatientRequestForm(forms.ModelForm):
    captcha = ReCaptchaField(
        label="",
    )

    class Meta:
        model = PatientRequest
        fields = [
        # Identification
        "first_name",
        "last_name",
        "email",
        "phone",
        # Treatment
        "treatment_schema",
        "available_treatment",
        "cd4_amount",
        "viral_load",
        "other_affections",
        "medical_urgencies",
        # Logistic
        "route",
        "location",
        "location_details",
        # Other
        "other_details",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if not settings.RECAPTCHA_PUBLIC_KEY:
            del self.fields["captcha"]

