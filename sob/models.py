from django.db import models

# Create your models here.

# fieldで検索してそれに合ったものを探す
class SobModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class SearchModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)

    def __str__(self):
        return self.title
