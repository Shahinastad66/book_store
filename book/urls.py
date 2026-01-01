from django.urls import path
from book.views import *


urlpatterns = [
    path('show', show_book),
    path('insert', insert_book),
    path('index', index)
]
