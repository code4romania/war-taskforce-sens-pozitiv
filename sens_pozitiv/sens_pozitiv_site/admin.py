from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import EmailTemplate


@admin.register(EmailTemplate)
class AdminEmailTemplate(admin.ModelAdmin):
    list_display = ["template", "lang"]
    readonly_fields = ["template", "lang"]

    def has_module_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
