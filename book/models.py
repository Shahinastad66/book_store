from django.db import models


class Book(models.Model):

    CATEGORY_CHOICES = [
        ('SC', 'Science'),
        ('FN', 'Fun'),
        ('HC', 'Historical'),
    ]

    name = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.FloatField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

