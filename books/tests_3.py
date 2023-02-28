from django.db.models.signals import post_save, post_delete
from django.test import TestCase

from books.models import Author, Book


class Question3TestCase(TestCase):
    def test_book_signals(self):
        a1 = Author.objects.create(name="Author 1")
        a2 = Author.objects.create(name="Author 2")
        self.assertEqual(a1.book_count, 0)
        self.assertEqual(a2.book_count, 0)

        Book.objects.create(title="Book1", isbn="1", author=a1)
        a1.refresh_from_db()
        self.assertEqual(a1.book_count, 1)
        self.assertEqual(a2.book_count, 0)

        Book.objects.create(title="Book2", isbn="2", author=a1)
        a1.refresh_from_db()
        self.assertEqual(a1.book_count, 2)
        self.assertEqual(a2.book_count, 0)

        Book.objects.filter(title="Book2").delete()
        a1.refresh_from_db()
        self.assertEqual(a1.book_count, 1)
        self.assertEqual(a2.book_count, 0)

    def test_signal_setup(self):
        self.assertTrue(post_save.has_listeners(Book))
        self.assertTrue(post_delete.has_listeners(Book))

        self.assertFalse(post_save.has_listeners(Author))
        self.assertFalse(post_delete.has_listeners(Author))
