from django.contrib import admin
from django.urls import path
from book.views import BookView, BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BookView.as_view()),
    path('<int:pk>', BookDetailView.as_view())
]
