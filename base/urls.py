from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view()),
]

""" path('about', views.about, name="about"),
    path('portfolio', views.projects, name="portfolio"),
    path('contact', views.contact, name="contact"), """