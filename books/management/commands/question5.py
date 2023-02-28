from django.core.management import BaseCommand

from books.helpers import setup_author_notify_schedule


class Command(BaseCommand):
    help = "Run the setup_author_notify_schedule function"

    def handle(self, *args, **options):
        setup_author_notify_schedule()
        print("setup_author_notify_schedule was run")
