import logging

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__file__)

DEFAULT_USER_GROUP = "Users"


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    TYPES_CHOICES = (
        (1, _("Individual")),
        (2, _("Corporate")),
        (3, _("Non-Profit")),
        (4, _("Government")),
    )

    email = models.EmailField(_("email address"), unique=True)

    type = models.SmallIntegerField(_("type"), choices=TYPES_CHOICES, default=1)
    phone_number = models.CharField(_("phone number"), max_length=13, null=True, blank=True)
    address = models.CharField(_("address"), max_length=255, blank=True, null=True)
    details = models.JSONField(_("details"), null=True, blank=True)
    description = models.CharField(
        _("general user description"),
        default="",
        blank=True,
        null=False,
        max_length=500,
    )

    is_validated = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        self.username = self.email
        self.is_staff = True  # needed to be able to login to admin
        super(CustomUser, self).save(*args, **kwargs)
        # all new users are added by default in the users group
        try:
            if not self.is_superuser:
                self.groups.add(Group.objects.get(name=DEFAULT_USER_GROUP))
        except Group.DoesNotExist:
            logger.warn(f"Could Not add group {DEFAULT_USER_GROUP} for user {self.username} !")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    get_full_name.short_description = _("Full Name")
