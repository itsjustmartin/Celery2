from django.core.management import BaseCommand

from books.helpers import setup_book_count_update_schedule


class Command(BaseCommand):
    help = "Run the setup_book_count_update_schedule function"

    def handle(self, *args, **options):
        setup_book_count_update_schedule()
        print("setup_book_count_update_schedule was run")
