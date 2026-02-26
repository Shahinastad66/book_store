from rest_framework import serializers
from book.models import Book, ImageBook
import datetime

class BookSerializer(serializers.ModelSerializer):
    total_images = serializers.IntegerField(read_only=True)

    def to_internal_value(self, data):
        data["published_date"] = datetime.datetime.now().date()
        result = super().to_internal_value(data=data)
        return result
    
    def validate(self, attrs):
        if True:
            res = super().validate(attrs=attrs)
            return res

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Book
        fields = ["name", "published_date", "price", "category", "total_images"]
        read_only_fields = ("total_images",)


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
        fields = ['image', 'name']