from django.contrib import admin
from django.urls import path, include
from webapp.views import openai

urlpatterns = [
    path('correcao/', openai.correcao)
]