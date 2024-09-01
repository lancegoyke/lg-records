import random
from textwrap import dedent

from django.core.management.base import BaseCommand, CommandParser
from django.contrib.sites.models import Site

from allauth.socialaccount.models import SocialApp

from challenges.models import Challenge
from users.models import CustomUser as User


class Command(BaseCommand):
    help = "Seeds the database with an initial superuser and Challenge object"

    def add_arguments(self, parser: CommandParser) -> None:
        super().add_arguments(parser)
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete all existing data before seeding the database",
        )

    def _create_challenges(self) -> list[Challenge]:
        """Returns a Challenge object, but does not save it to the databse."""
        num_objects = 25
        challenges = []
        for n in range(num_objects):
            name = f"Challenge {n + 1}"
            description = dedent(
                f"""\
                Bodyweight squat x {random.randint(5, 20)}
                Push up x {random.randint(5, 20)}
                Walking lunge x {random.randint(5, 20)} each
                Burpees x {random.randint(5, 20)}
                Front plank x 30 sec
                """
            )
            challenge = Challenge(name=name, description=description)
            challenges.append(challenge)
        return Challenge.objects.bulk_create(challenges)

    def _create_social_app(self) -> None:
        """Creates a SocialApp object for the Django admin."""
        site = Site.objects.get_current()
        google = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id="1234567890",
            secret="0987654321",
        )
        google.sites.add(site)
        google.save()

    def _create_superuser(self) -> User:
        return User.objects.create_superuser(
            "admin", "admin@example.com", "adminpassword"
        )

    def _create_users(self) -> list[User]:
        num_users = 100
        return User.objects.bulk_create(
            [
                User(username=self._rand_username(), password="testpass123")
                for _ in range(num_users)
            ]
        )

    def _rand_username(self) -> str:
        ALPHAS = "abcdefghijklmnopqrstuvwxyz"
        ALPHAS += ALPHAS.upper()
        NUMS = "1234567890"
        return f"{random.choice(ALPHAS + NUMS)}{random.choice(ALPHAS + NUMS)}{random.choice(ALPHAS + NUMS)}{random.choice(ALPHAS + NUMS)}{random.choice(ALPHAS + NUMS)}"  # noqa

    def handle(self, *args, **kwargs):
        if kwargs["delete"]:
            User.objects.all().delete()
            Challenge.objects.all().delete()
            SocialApp.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("All data deleted"))

        if (
            User.objects.exists()
            or Challenge.objects.exists()
            or SocialApp.objects.exists()
        ):
            self.stdout.write(
                self.style.WARNING(
                    "Data already exists. Use --delete to delete all data first"
                )
            )
            return

        self._create_superuser()
        self._create_users()
        self._create_challenges()
        self._create_social_app()

        self.stdout.write(self.style.SUCCESS("Data created successfully"))
