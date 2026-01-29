from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework import generics

def show_book(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

def index(request):
    books = Book.objects.all()
    return render(request, template_name="books.html", context={"books" : books})

class BookAPI(APIView):
    def post(self, request):
        body = json.loads(request.body.decode("utf-8"))
        body["published_date"] = datetime.datetime.now().date()
        serializer = BookSerializer(data=body)
        if serializer.is_valid():
            book = serializer.save()
            return JsonResponse ({"book_id" : book.id}) 
        return JsonResponse({"error" : "Data Format Is Not Correct"})
    
    def get(self, request):
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)

    def delete(self, request):
        pass

class BookGenericAPI(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class GetBookAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"