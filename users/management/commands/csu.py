from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@shoper.com',
            first_name='Admin',
            last_name='Adminich',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('123123')
        user.save()
