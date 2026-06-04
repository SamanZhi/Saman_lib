from django.shortcuts import render, redirect
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

def book_create_update(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(request, 'library_app/book_form.html', {'form': form})