from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(null=True)
    thumbnailUrl = models.CharField(max_length=255, null=True)
    shortDescription = models.CharField(max_length=2505, null=True)
    longDescription = models.TextField(null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.body[0:15]} {self.book_id} ' 
