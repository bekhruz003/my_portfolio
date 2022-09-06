from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeModel


class HomeView(ListView):
    template_name = 'index.html'
    model = HomeModel
