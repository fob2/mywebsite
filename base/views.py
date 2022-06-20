from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class Home(TemplateView):
    template_name = 'mywebsite/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['about'] = About.objects.first()
        context['portfolio'] = Portfolio.objects.all()
        return context
