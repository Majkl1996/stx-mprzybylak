from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['date_of_publication']


class BookSearchForm(forms.Form):
    search = forms.CharField(
        label="Search for a book", required=False,
        widget=forms.TextInput(attrs={'class': "field__input", 'id': 'search', 'autofocus': True}))
    author = forms.CharField(
        label="Search for an author", required=False,
        widget=forms.TextInput(attrs={'class': "field__input", 'id': 'author'}))
