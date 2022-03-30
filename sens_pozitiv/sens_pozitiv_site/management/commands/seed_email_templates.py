from django.core.management.base import BaseCommand

from sens_pozitiv_site.models import EmailTemplate

TEMPLATE_EN = """Hi,

The request for patient "{{ pr.first_name }} {{ pr.last_name }}" was received with the following data:


First Name: {{ pr.first_name }}
Last Name: {{ pr.last_name }}
Email: {{ pr.email }}

Treatment Schema: {{ pr.treatment_schema }}
Available Treatment: {{ pr.available_treatment }}
CD4 Amount: {{ pr.cd4_amount }}
Viral Load: {{ pr.viral_load }}
Other Affections: {{ pr.other_affections }}
Medical Urgencies: {{ pr.medical_urgencies }}

Logistic:

Route: {{ pr.route }}
Current Location: {{ pr.location }}
Current Location Details: {{ pr.location_details }}

Other Details:

{{ pr.other_details }}

Thank you!
Positive Sense Romania
"""

TEMPLATE_RO = """Bună,

Cererea de înscriere a pacientului "{{ pr.first_name }} {{ pr.last_name }}" a fost primită cu următoarele date:

Prenume: {{ pr.first_name }}
Nume: {{ pr.last_name }}
Email: {{ pr.email }}

Schemă de tratament: {{ pr.treatment_schema }}
Tratament Disponibil: {{ pr.available_treatment }}
Număr CD4: {{ pr.cd4_amount }}
încarcare virală: {{ pr.viral_load }}
Alte afecțiuni cronice sau condiții de viață: {{ pr.other_affections }}
Urgențe medicale asociate HIV sau altele: {{ pr.medical_urgencies }}

Informații Logistice:

Traseu: {{ pr.route }}
Locația Curentă: {{ pr.location }}
Detalii suplimentare despre locație: {{ pr.location_details }}

Alte Detalii:

{{ pr.other_details }}

Mulțumim!
Sens Pozitiv Romania
"""


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--replace",
            action="store_true",
            help="Replace existing templates",
        )

    def handle(self, *args, **options):
        for lang in ["en", "ro", "uk", "ru"]:
            template, created = EmailTemplate.objects.get_or_create(template="patient_request", lang=lang)

            if created or options["replace"]:
                template.text_content = TEMPLATE_RO if lang == "ro" else TEMPLATE_EN
                template.save()
