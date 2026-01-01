from django import forms
from book.models import Book


# class CreateBook(forms.Form):
#     name = forms.CharField(max_length=100)
#     published_date = forms.DateField()
#     price = forms.FloatField()
#     category = forms.CharField(max_length=2)

class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"