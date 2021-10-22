from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import RedirectView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import hero
from markdown import markdown

class HeroView(RedirectView):
    url = '/hero/'

class HomeView(TemplateView):
    template_name = 'home.html'
    model = hero

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = hero

class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = hero

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = 'hero_new.html'
    model = hero
    fields = ['name', 'identity', 'strengths', 'weakness', 'description', 'image']

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'hero_edit.html'
    model = hero
    fields = ['name', 'identity', 'strengths', 'weakness', 'description', 'image']

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')

# class DocumentView(TemplateView):
#     template_name = 'document.html'

#     def get_context_data(self, **kwargs):
#         document = self.kwargs.get('doc', 'Index')
#         markdown_text = open(f'Documents/{document}.md').read()
#         return dict(doc=markdown(markdown_text), file=document)