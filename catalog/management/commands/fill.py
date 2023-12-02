from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'name': 'Category1'},
            {'name': 'Category2'},
            {'name': 'Category3'},
            {'name': 'Category4'},
            {'name': 'Category12'},
            {'name': 'Category13'},
            {'name': 'Category23'}
        ]

        category_to_create = [Category(**category) for category in category_list]
        Category.objects.all().delete()
        Category.objects.bulk_create(category_to_create)
