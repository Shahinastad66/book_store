from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from book.models import Book, ImageBook
from book.serializers import BookSerializer, ImageBookUploadSerializer
from book.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

class CustomBookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  
    max_page_size = 10 


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Book.objects.filter(publisher=user)
        return Book.objects.none()

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


    @action(detail=True, methods=['post'], url_path='add-image')
    def add_image(self, request, pk=None):
        book = self.get_object()
        serializer = ImageBookUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PublishedBooksAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] 

    def get_queryset(self):

        return Book.objects.filter(
            is_published=True
        ).select_related('publisher').prefetch_related('images')



class MyBooksAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomBookPagination


    def get_queryset(self):
        return Book.objects.filter(publisher=self.request.user).prefetch_related('images')