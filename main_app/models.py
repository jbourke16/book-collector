from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    release_year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

