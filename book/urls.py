from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet, PublishedBooksAPI, MyBooksAPI


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book') 
router.register(r'published-books', PublishedBooksAPI, basename='published-book') 
router.register(r'my-books', MyBooksAPI, basename='my-book') 

urlpatterns = [
    path('', include(router.urls)),
]
