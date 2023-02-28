from django.test import TestCase
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from books.helpers import setup_book_count_update_schedule


class Question4TestCase(TestCase):
    def test_book_count_update_schedule(self):
        setup_book_count_update_schedule()
        interval_schedules = IntervalSchedule.objects.all()
        self.assertEqual(interval_schedules.count(), 1)
        interval_schedule = interval_schedules.first()
        self.assertEqual(interval_schedule.every, 1)
        self.assertEqual(interval_schedule.period, IntervalSchedule.DAYS)

        pt = PeriodicTask.objects.get(interval=interval_schedule)
        self.assertEqual(pt.task, "books.tasks.author_count_update")
