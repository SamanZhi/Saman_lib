from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def book_list(request=HttpRequest):
    return render(request=HttpResponse)

def book_detail(request=HttpRequest):
    return render(request=HttpResponse)

def book_create_update(request=HttpRequest):
    return render(request=HttpResponse)

