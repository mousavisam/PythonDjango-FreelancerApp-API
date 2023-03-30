from django.core.management import BaseCommand

from main.shared.initial_data.category.generate_categories import GenerateCategories


class Command(BaseCommand):
    help = "generate categories "

    def handle(self, *args, **options):
        categories = GenerateCategories()
        categories.add_new_categories()
