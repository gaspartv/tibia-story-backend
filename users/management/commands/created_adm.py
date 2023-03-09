from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Created admin"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            type=str,
            help="indicate the name of the adm to be created",
        )
        parser.add_argument(
            "--password",
            type=str,
            help="indicate the password of the adm to be created",
        )
        parser.add_argument(
            "--email",
            type=str,
            help="indicate the email to be created",
        )

    def handle(self, *args, **kwargs):
        user = kwargs["username"]
        password = kwargs["password"]

        email = kwargs["email"]

        User.objects.create_superuser(username=user, password=password, email=email)
