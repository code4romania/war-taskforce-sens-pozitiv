from django.conf import settings
from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from dispatch.models import Clinic, Contact, Service, PatientRequest


class ContactInLine(admin.StackedInline):
    model = Contact
    extra = 1
    verbose_name_plural = _("Contacts")


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1
    verbose_name_plural = _("Services")


@admin.register(Clinic)
class AdminClinic(ImportExportModelAdmin):

    list_per_page = settings.LIST_PER_PAGE
    ordering = ("pk",)

    list_display = [
        "name",
        "region",
    ]

    list_display_links = [
        "name",
    ]

    list_filter = [
        "region",
    ]

    search_fields = [
        "name",
        "region",
    ]

    inlines = [
        ContactInLine,
        ServiceInline,
    ]

    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 4, "cols": 63})},
    }


@admin.register(PatientRequest)
class PatientRequestAdmin(ImportExportModelAdmin):

    list_per_page = settings.LIST_PER_PAGE
    ordering = ("pk",)

    list_display = [
        "full_name",
        "email",
        "phone",

        "cd4_amount",
        "viral_load",

        "clinic",

        "route",
        "location",
    ]

    list_display_links = [
        "full_name",
    ]

    search_fields = [
        "full_name",
        "email",
        "phone",
        "other_affections",
        "medical_urgencies",
        "location_details",
        "other_details",
        "cd4_amount",
        "viral_load",
        "clinic",
        "route",
        "location",
    ]

    list_filter = [
        "cd4_amount",
        "viral_load",
        "clinic",
        "route",
        "location",
    ]

    fieldsets = (
        (
            _("Identification"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                )
            }
        ),
        (
            _("Treatment"),
            {
                "fields": (
                    "treatment_schema",
                    "available_treatment",
                    "cd4_amount",
                    "viral_load",
                    "other_affections",
                    "medical_urgencies",
                )
            }
        ),
        (
            _("Clinic"),
            {
                "fields": (
                    "clinic",
                )
            }
        ),
        (
            _("Logistic"),
            {
                "fields": (
                    "route",
                    "location",
                    "location_details",
                )
            }
        ),
        (
            _("Other"),
            {
                "fields": (
                    "other_details",
                )
            }
        ),
    )