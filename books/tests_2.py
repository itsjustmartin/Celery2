from unittest import mock

from django.test import TestCase

from books.models import Author
from books.tasks import author_count_update


class Question2TestCase(TestCase):
    def test_shared_task_used(self):
        from books.tasks import shared_task

        self.assertIsNotNone(
            shared_task
        )  # assume if it's imported there then it's used as the decorator

    def test_author_count_update_is_task(self):
        self.assertIsNotNone(author_count_update.delay)

    @staticmethod
    def test_author_count_update_behaviour():
        a1 = Author.objects.create(name="Author 1")
        a2 = Author.objects.create(name="Author 2")
        a3 = Author.objects.create(name="Author 3")
        a4 = Author.objects.create(name="Author 4")
        with mock.patch(
            "books.tasks.update_count_for_author"
        ) as update_count_for_author:
            author_count_update()
            update_count_for_author.assert_any_call(a1)
            update_count_for_author.assert_any_call(a2)
            update_count_for_author.assert_any_call(a3)
            update_count_for_author.assert_any_call(a4)
