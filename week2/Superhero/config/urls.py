from django.contrib import admin
from django.urls import path
from hero.views import HulkView, IronManView , BlackWidowView, HerosView

urlpatterns = [
    path('hero', HerosView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidowView.as_view()),
    
]
