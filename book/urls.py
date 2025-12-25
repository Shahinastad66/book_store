from django.urls import path
from book.views import show_book

urlpatterns = [
    path('', show_book),
]
