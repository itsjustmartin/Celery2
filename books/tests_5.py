import json

from django.test import TestCase
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from books.helpers import setup_author_notify_schedule
from books.tasks import author_notify


class Question5TestCase(TestCase):
    def test_author_notify_is_task(self):
        self.assertIsNotNone(author_notify.delay)

    def test_author_notify_schedule(self):
        setup_author_notify_schedule()
        crontab_schedules = CrontabSchedule.objects.all()
        self.assertEqual(crontab_schedules.count(), 1)
        crontab_schedule = crontab_schedules.first()
        self.assertEqual(crontab_schedule.minute, "0")
        self.assertEqual(crontab_schedule.hour, "6")
        self.assertEqual(crontab_schedule.day_of_week, "*")
        self.assertEqual(crontab_schedule.day_of_month, "1")
        self.assertEqual(crontab_schedule.month_of_year, "*")

        pt = PeriodicTask.objects.get(crontab=crontab_schedule)
        self.assertEqual(pt.task, "books.tasks.author_notify")
        self.assertEqual(json.loads(pt.args), [True])
