from django.db import models


class Author(models.Model):
    name = models.TextField(unique=True)
    book_count = models.PositiveIntegerField(default=0)


class Book(models.Model):
    title = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
