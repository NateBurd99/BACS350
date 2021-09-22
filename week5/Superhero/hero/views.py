from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import hero

class HeroView(ListView):
    template_name = 'hero_list.html'
    model = hero

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = hero