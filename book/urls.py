from django.urls import path
from book.views import *


urlpatterns = [
    path('show', show_book),
    path('index', index),
    path('create', BookAPI.as_view()),
    path('book-generic', BookGenericAPI.as_view()),
    path('get-book/<int:id>', GetBookAPI.as_view()),
]
