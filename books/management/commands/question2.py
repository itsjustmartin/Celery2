from django.core.management import BaseCommand

from books.tasks import author_count_update


class Command(BaseCommand):
    help = "Run the author_count_update function using Celery"

    def handle(self, *args, **options):
        author_count_update.delay()
        print("author_count_update was run")
