from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name