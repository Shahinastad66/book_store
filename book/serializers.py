from rest_framework import serializers
from book.models import Book, ImageBook
import datetime

class ImageBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBook
        fields = ['id', 'name', 'image']

class BookSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(source='publisher.username', read_only=True)
    images = ImageBookSerializer(many=True, read_only=True)
    total_images = serializers.IntegerField(source='images.count', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'name', 'published_date', 'price', 'category',
            'publisher', 'publisher_name', 'is_published',
            'images', 'total_images'
        ]
        read_only_fields = ('publisher', 'total_images', 'images')

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['publisher'] = request.user
        return super().create(validated_data)


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'name', 'author', 'published_date', 'price', 'currency',
            'category', 'page_count', 'description', 'is_published'
        ]


class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'name', 'author', 'published_date', 'price', 'currency',
            'category', 'page_count', 'description', 'is_published'
        ]


class ImageBookUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBook
        fields = ['name', 'image']