from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from django.views.generic import RedirectView, TemplateView
from doc.views import DocumentView

urlpatterns = [
    path('', DocumentView.as_view(), name='document'),
    path('<str:doc>', DocumentView.as_view()),
    ]