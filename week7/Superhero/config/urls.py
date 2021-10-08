from django.contrib import admin
from django.urls import path
from hero.views import HeroView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView, HomeView
from django.urls.conf import include, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/', HeroListView.as_view(), name='hero_list'),
    path('hero/add', HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),

]
