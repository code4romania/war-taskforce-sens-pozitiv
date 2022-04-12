from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import include, path, re_path
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import RedirectView

from .views import PatientRegisterRequestCreateView

admin.site.site_title = settings.ADMIN_TITLE
admin.site.site_header = settings.ADMIN_TITLE
admin.site.index_title = settings.ADMIN_TITLE_SHORT


urlpatterns = i18n_patterns(
    # URL patterns which accept a language prefix
    path(
        _("request-form/"),
        PatientRegisterRequestCreateView.as_view(),
        name="patient_request_form",
    ),
    # Redirect / to /admin
    path("", RedirectView.as_view(url="admin/"), name="home"),
    path(
        "admin/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "admin/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "admin/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "admin/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("admin/", admin.site.urls, name="admin"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("i18n/", include("django.conf.urls.i18n")),
    # DPD
    # path("dpd/", include("django_plotly_dash.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
