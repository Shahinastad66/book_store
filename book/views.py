from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from book.forms import CreateBook 

def show_book(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

@csrf_exempt
def insert_book(request):
    if request.method == "POST":
        print(request.POST)
        body = json.loads(request.body.decode("utf-8"))
        body["published_date"] = datetime.datetime.now()
        form = CreateBook(body)
        if form.is_valid():
            book = form.save()
            return JsonResponse ({"book_id" : book.id}) 
        return JsonResponse({"error" : "Data Format Is Not Correct"})
    elif request.method == "GET":
        books = list(Book.objects.values())

        return JsonResponse(books, safe=False)
    
def index(request):
    books = Book.objects.all()
    return render(request, template_name="books.html", context={"books" : books})