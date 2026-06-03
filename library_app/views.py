from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'library_app/main.html')

def book_list(request):
    return render(request, 'library_app/book_list.html')

def book_detail(request):
    return render(request, 'library_app/book_detail.html')

def book_create_update(request):
    return render(request, 'library_app/book_form.html')

