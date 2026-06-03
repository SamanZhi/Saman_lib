from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('book_list/', views.book_list, name='book_list'),
    # path('book_detail/', views.book_detail, name='book_detail'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('book_form/', views.book_create_update, name='book_form'),
]