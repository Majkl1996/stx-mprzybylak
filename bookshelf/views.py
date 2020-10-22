from django.shortcuts import render, redirect
import requests

from .models import Book
from .forms import AddBookForm, BookSearchForm

key = 'AIzaSyDn7RdEeFhlGpO-4KTVWz57_uJQuZD9oJk'


def books(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('title')
        if ' ' not in books:
            return render(request, "books.html", {"message": "Sorry, no books in here"})
        return render(request, "books.html", locals())


def addbook(request):
    form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    context = {'form': form}
    return render(request, 'book_form.html', context)


def editbook(request, pk):
    book = Book.objects.get(pk=pk)
    form = AddBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'book_form.html', {'form': form})


def search(request):
    form = BookSearchForm()
    return render(request, 'search.html', {'form': form})


def result(request):

    author = request.GET.get('author', False)
    search = author if request.GET.get(
        'search', False) == "" else request.GET.get('search', False)

    if (search == False and author == False) or (search == "" and author == ""):
        return redirect('result')

    queries = {'q': search, 'inauthor': author, 'key': key}
    print(queries)
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)
    print(r)
    if r.status_code != 200:
        return render(request, 'search.html',
                      {'message': 'Sorry, there seems to be an issue with Google Books right now.'})

    data = r.json()

    if 'items' not in data:
        return render(request, 'search.html', {'message': 'Sorry, no books match that search term.'})

    fetched_books = data['items']
    books = []
    for book in fetched_books:
        book_dict = {
            'title': book['volumeInfo']['title'],
            'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
            'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
            'info': book['volumeInfo']['infoLink'],
            'popularity': book['volumeInfo']['ratingsCount'] if 'ratingsCount' in book['volumeInfo'] else 0
        }
        books.append(book_dict)

    def sort_by_pop(e):
        return e['popularity']

    books.sort(reverse=True, key=sort_by_pop)

    return render(request, 'result.html', {'books': books})
