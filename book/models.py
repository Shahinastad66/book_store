from django.db import models
from django.conf import settings

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
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='published_books', null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ImageBook(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="images")

    def __str__(self):
        return self.name
    
