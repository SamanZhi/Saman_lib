from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def main(request):
    return render(request, 'library_app/main.html')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library_app/book_list.html', context)

def book_detail(request, id):
    details = Book.objects.get(id=id)
    context = {'details': details}
    return render(request, 'library_app/book_detail.html', context)


def book_create_update(request, id=None):

    if id:
        book = get_object_or_404(Book, id=id)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'library_app/book_form.html',
        {'form': form}
    )