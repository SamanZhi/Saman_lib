from django.shortcuts import render
from .models import Book

# Create your views here.
def main(request):
    return render(request, 'library_app/main.html')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library_app/book_list.html', context)

def book_detail(request):
    details = Book.objects.get(id=id)
    context = {'details': details}
    return render(request, 'library_app/book_detail.html', context)

def book_create_update(request):
    return render(request, 'library_app/book_form.html')

