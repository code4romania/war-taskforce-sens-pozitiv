from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from app_account.models import DEFAULT_USER_GROUP

DEFAULT_USER_GROUP_PERMISSIONS = [
    "view_patientrequest",
    "add_patientrequest",
    "change_patientrequest",
    "delete_patientrequest",
    "view_clinic",
    "add_clinic",
    "change_clinic",
    "delete_clinic",
    "view_service",
    "add_service",
    "change_service",
    "delete_service",
    "view_contact",
    "add_contact",
    "change_contact",
    "delete_contact",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_group, _ = Group.objects.get_or_create(name=DEFAULT_USER_GROUP)
        users_group.permissions.set(
            Permission.objects.filter(codename__in=DEFAULT_USER_GROUP_PERMISSIONS).values_list("id", flat=True)
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"'{DEFAULT_USER_GROUP}' group has been created and appropriate permissions were assigned"
            )
        )
