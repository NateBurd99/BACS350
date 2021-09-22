from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book

class BookView(ListView):
    template_name = 'book_list.html'
    model = Book

class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book