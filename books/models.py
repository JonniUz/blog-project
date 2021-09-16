from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(null=True)
    shortDescription = models.CharField(max_length=2505, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField('Author')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/review', null=True, blank=True)

    def __str__(self):
        return f'{self.body[0:15]} {self.book_id} '


class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
