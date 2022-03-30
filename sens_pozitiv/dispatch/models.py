
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


ROUTE_CHOICES = (
    ("ROM", _("Stays in Romania")),
    ("TRA", _("In Transit")),
    ("UNK", _("Unsure"))
)

CURRENT_LOCATION_CHOICES = (
    ("RO", _("Romania")),
    ("UA", _("Ukraine")),
    ("MD", _("Moldavia")),
    ("OTH", _("Other")),
)


class Clinic(models.Model):

    name = models.CharField(_("Medical Center Name"), max_length=255, blank=False)
    region = models.CharField(_("Region"), max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} - {self.region}"

    def validate_unique(self, exclude=None):
        try:
            super().validate_unique()
        except ValidationError as e:
            raise ValidationError(_("There is already a Clinic with this name and region"))

    class Meta:
        unique_together = ["name", "region"]

        verbose_name = _("Clinic")
        verbose_name_plural = _("Clinics")


class Contact(models.Model):

    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)

    name = models.CharField(_("Contact Person Name"), max_length=255, blank=False)
    role = models.CharField(_("Contact Person Role"), max_length=255, blank=True)
    email = models.EmailField(_("Contact Person Email"), blank=True)
    phone = PhoneNumberField(verbose_name=_("Contact Person Phone Number"), blank=True, help_text=_("e.g. +40723000123"))

    def __str__(self):
        return f"{self.name} - {self.role}" if self.role else self.name

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Service(models.Model):

    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)

    # Medication
    medication_name = models.CharField(_("Medication Name"), max_length=255, blank=False)
    medication_quantity = models.CharField(_("Medication Quantity"), max_length=255, blank=True)
    medication_details = models.TextField(_("Medication Details"), blank=True)
    # Medical Services
    med_service_type = models.CharField(_("Medical Service Type"), max_length=255, blank=False)
    med_service_quantity = models.CharField(_("Medical Service Quantity"), max_length=255, blank=True)
    med_service_details = models.TextField(_("Medical Service Details"), blank=True)
    # Other Services
    other_service_type = models.CharField(_("Non-Medical Service Type"), max_length=255, blank=False)
    other_service_quantity = models.CharField(_("Non-Medical Service Quantity"), max_length=255, blank=True)
    other_service_details = models.TextField(_("Non-Medical Service Details"), blank=True)

    def __str__(self):
        return f"{self.medication_name} - {self.med_service_type} - {self.other_service_type}"

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class PatientRequest(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    # Identification
    first_name = models.CharField(_("First Name"), max_length=255, blank=False)
    last_name = models.CharField(_("Last Name"), max_length=255, blank=False)
    email = models.EmailField(_("Email"), blank=False)
    phone = PhoneNumberField(verbose_name=_("Phone Number"), blank=False, help_text=_("e.g. +40723000123"))

    # Treatment
    treatment_schema = models.TextField(_("Treatment Schema"), blank=False)
    available_treatment = models.CharField(_("Available Schema"), max_length=100, blank=False, help_text=_("For how long do you have treatment available?"))
    cd4_amount = models.CharField(_("CD4 Amount"), max_length=100, blank=False, help_text=_("CD4 at last check"))
    viral_load = models.CharField(_("Viral Load"), max_length=100, blank=False, help_text=_("Last measured viral load"))
    other_affections = models.TextField(_("Other Affections"), blank=False, help_text=_("Other affections or life conditions"))
    medical_urgencies = models.TextField(_("Medical Urgencies"), blank=False, help_text=_("Medical urgencies related to HIV or other"))

    # Clinic
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)

    # Logistic
    route = models.CharField(_("Route"), max_length=3, blank=False, choices=ROUTE_CHOICES, default="ROM")
    location = models.CharField(_("Current Location"), max_length=3, blank=False, choices=CURRENT_LOCATION_CHOICES, default="RO")
    location_details = models.TextField(_("Current Location Details"), blank=True, help_text=_("County, Town and other relevant details"))

    # Other
    other_details = models.TextField(_("Other Details"), blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.short_description = _("Full Name")

    def validate_unique(self, exclude=None):
        try:
            super().validate_unique()
        except ValidationError as e:
            raise ValidationError(_("There is already a Patient with this name and email"))


    def __str__(self):
        return f"{self.full_name()} "

    class Meta:
        unique_together = ["first_name", "last_name", "email"]

        verbose_name = _("Patient Request")
        verbose_name_plural = _("Patient Requests")