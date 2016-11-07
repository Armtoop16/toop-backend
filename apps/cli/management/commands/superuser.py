# Core Django imports
from django.core.management.base import BaseCommand

# Local apps imports
from apps.core.accounts.helpers import create_or_update_superuser


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_or_update_superuser()
