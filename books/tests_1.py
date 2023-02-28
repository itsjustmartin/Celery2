from django.conf import settings
from django.test import TestCase


class Question1TestCase(TestCase):
    def test_celery_settings(self):
        self.assertIn("django_celery_results", settings.INSTALLED_APPS)
        self.assertEqual(settings.CELERY_RESULT_BACKEND, "django-db")
        self.assertEqual(settings.CELERY_BROKER_URL, "redis://localhost:6379/0")
