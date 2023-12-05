from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'name': 'product', 'description': 'Something tangible I could sell to client'},
            {'name': 'service', 'description': 'Something I would do for client'},
        ]

        category_to_create = [Category(**category) for category in category_list]
        Category.objects.all().delete()
        Category.objects.bulk_create(category_to_create)
        product_list = [
            {
                'name': 'Site',
                'description': 'You could buy your own site! How cool is that?',
                'category': category_to_create[0],
                'price': '69',
             },
            {
                'name': 'Prebuild PC',
                'description': 'Hey! It\'s Fing PC with unicorn puke allover it! You should buy that',
                'category': category_to_create[0],
                'price': '420',
            },
            {
                'name': 'Teach me Physics ',
                'description': 'Hey, I could teach you some physics if you wont, I legally can do that',
                'category': category_to_create[1],
                'price': '20',
            },
            {
                'name': 'Let\'s chat',
                'description': 'Come to my twich, we can chat there!',
                'category': category_to_create[1],
                'price': '0',
            }
        ]

        product_to_create = [Product(**product) for product in product_list]
        Product.objects.all().delete()
        Product.objects.bulk_create(product_to_create)
