from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from challenges.models import Challenge


User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds the database with an initial superuser and Challenge object'

    def handle(self, *args, **kwargs):
        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

        # Create a Challenge object
        challenge_name = 'Initial Challenge'
        if not Challenge.objects.filter(name=challenge_name).exists():
            Challenge.objects.create(name=challenge_name, description='This is the first challenge')
            self.stdout.write(self.style.SUCCESS(f'Challenge "{challenge_name}" created successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Challenge "{challenge_name}" already exists'))
