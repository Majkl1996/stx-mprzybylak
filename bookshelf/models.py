from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date_of_publication = models.DateField(auto_now_add=True)
    isbn = models.IntegerField()
    number_of_pages = models.IntegerField()
    cover_url = models.URLField()
    language = models.CharField(max_length=32)

    def __str__(self):
        return self.title
