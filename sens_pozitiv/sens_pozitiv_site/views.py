import re

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template
from django.urls import reverse
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from dispatch.models import PatientRequest
from sens_pozitiv_site.forms import PatientRequestForm
from sens_pozitiv_site.models import EmailTemplate

TAG_RE = re.compile(r"<[^>]+>")


class PatientRegisterRequestCreateView(SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = PatientRequest
    form_class = PatientRequestForm
    success_message = _("Thank you for registering the patient! The form you filled in has reached us.")
    failure_message = _(
        "There was an error submitting your request. Please try again or contact the site administrator."
    )

    def get_success_url(self):
        return reverse("patient_request_form")

    def get_success_message(self, cleaned_data):
        try:
            patient_request = PatientRequest.objects.get(
                first_name=cleaned_data["first_name"],
                last_name=cleaned_data["last_name"],
                email=cleaned_data["email"],
            )
        except PatientRequest.DoesNotExist:
            return self.failure_message
        else:
            send_email(
                template="patient_request",
                lang=get_language() or "en",
                context=Context({"pr": patient_request}),
                subject=_("PSD - Patient Request Form"),
                to=cleaned_data["email"],
            )
            if settings.NOTIFICATIONS_EMAIL:
                send_email(
                    template="patient_request",
                    lang="ro",
                    context=Context({"pr": patient_request}),
                    subject=_("PSD - Registration Form"),
                    to=settings.NOTIFICATIONS_EMAIL,
                )

        return self.success_message


def send_email(template, lang, context, subject, to):
    """
    Sends a single email

    :param template: One of the EMAIL_TEMPLATE_CHOICES from models
    :param context: A dict containing the dynamic values of that template
    :param subject: The subject of the email
    :param to: Destination email address
    :return: Message send result
    """
    try:
        tpl = EmailTemplate.objects.get(template=template, lang=lang)
    except EmailTemplate.DoesNotExist:
        return

    text_content = Template(tpl.text_content).render(context)
    msg = EmailMultiAlternatives(
        subject,
        text_content,
        settings.NOTIFICATIONS_REPLYTO_EMAIL,
        [to],
        headers={"X-SES-CONFIGURATION-SET": settings.NOTIFICATIONS_X_SES_CONFIGURATION_SET_HEADER},
    )

    if len(remove_tags(tpl.html_content).strip()) > 0:
        html_content = Template(tpl.html_content).render(context)
        msg.attach_alternative(html_content, "text/html")

    return msg.send(fail_silently=True)


def remove_tags(text):
    return TAG_RE.sub("", text)
