from django.shortcuts import render, get_object_or_404
from .models import Book 
# books = [
#     {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     {'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
#     {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
# ]

def home(request):
    data = {"books": Book.objects.all}
    print(data)
    return render(request, 'home.html', data)

def books_collection(request):
    return render(request, 'books.html')

def show(request, id):
    book = get_object_or_404(Book, pk=id)
    # book = list(filter(lambda book:book['id'] == id, books))
    data = {'book': book}
    print(book)
    print(data)
    return render(request, 'show.html', data)


def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)


def server_error_500(request):
    return render(request, '500.html')
