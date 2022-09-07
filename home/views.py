from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeModel, AboutModel, WorkModel


class HomeView(ListView):
    template_name = 'index.html'
    model = HomeModel

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['abouts'] = AboutModel.objects.all()
        data['works'] = WorkModel.objects.all()
        return data
