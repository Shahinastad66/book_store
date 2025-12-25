from django.shortcuts import render
from django.http import JsonResponse
from book.models import Book

def show_book(request):
    books = Book.objects.all()
    data = []
    for book in books:
        data.append({
            "id"             : book.id,
            "name"           : book.name,
            "published_date" : book.published_date,
            "price"          : book.price,
            "category"       : book.category
        })
    return JsonResponse(data, safe=False)
