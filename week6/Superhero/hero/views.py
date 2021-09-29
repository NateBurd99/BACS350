from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import RedirectView
from django.urls.base import reverse_lazy
from .models import hero

class HeroView(RedirectView):
    url = '/hero/'

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = hero

class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = hero

class HeroCreateView(CreateView):
    template_name = 'hero_new.html'
    model = hero
    fields = ['name', 'description']

class HeroUpdateView(UpdateView):
    template_name = 'hero_edit.html'
    model = hero
    fields = ['name', 'description']

class HeroDeleteView(DeleteView):
    model = hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')