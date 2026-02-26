from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework import generics
from django.db.models import Count
from rest_framework.permissions import AllowAny 
from book.paginations import LargeResultsSetPagination
from rest_framework import viewsets
from book.models import Book
from book.serializers import BookSerializer
from book.permissions import IsOwnerOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

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
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.annotate(total_images=Count("images"))
    pagination_class = LargeResultsSetPagination

class GetBookAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"