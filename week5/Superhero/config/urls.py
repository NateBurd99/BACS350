from django.contrib import admin
from django.urls import path
from hero.views import HeroView, HeroDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HeroView.as_view()),
    path('<int:pk>', HeroDetailView.as_view())

]
