from django.shortcuts import render, get_object_or_404, redirect
from .models import Book 
from django.contrib.auth.decorators import login_required
from .forms import BorrowBook


def home(request):
    data = {"books": Book.objects.all}
    print(data)
    return render(request, 'home.html', data)

def books_collection(request):
    return render(request, 'books.html')


@login_required
def show(request, id):
    book = get_object_or_404(Book, pk=id)
    # book = list(filter(lambda book:book['id'] == id, books))
    if request.method == 'POST':
        form = BorrowBook(request.POST)
        if form.is_valid():
            book.borrower = request.user
            book.save()
            return redirect('library-show', id=id)
    else:
        form = BorrowBook(initial={'borrower': request.user})
    data = {'book': book, 'form': form}
    # print(book)
    # print(data)
    return render(request, 'show.html', data)


def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)


def server_error_500(request):
    return render(request, '500.html')
