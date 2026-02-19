from django.db import models


class Book(models.Model):

    CATEGORY_CHOICES = [
        ('SC', 'Science'),
        ('FN', 'Fun'),
        ('HC', 'Historical'),
    ]

    name = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.IntegerField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class ImageBook(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="images")

    def __str__(self):
        return self.name