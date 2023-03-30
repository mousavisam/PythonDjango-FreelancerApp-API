from django.core.management import BaseCommand

from main.shared.initial_data.faq.generate_faq import GenerateFAQ


class Command(BaseCommand):
    help = "generate categories "

    def handle(self, *args, **options):
        generate_faq = GenerateFAQ()
        generate_faq.insert_faq()