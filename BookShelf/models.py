from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name