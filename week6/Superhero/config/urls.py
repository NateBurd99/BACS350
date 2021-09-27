from django.contrib import admin
from django.urls import path
from hero.views import HeroView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HeroView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/', HeroListView.as_view(), name='hero_list'),
    path('hero/add', HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),

]
