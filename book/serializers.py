from rest_framework import serializers
from book.models import Book
import datetime

class BookSerializer(serializers.ModelSerializer):

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
        fields = "__all__"