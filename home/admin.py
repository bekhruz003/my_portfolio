from django.contrib import admin
from .models import HomeModel, AboutModel, WorkModel


@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(WorkModel)
class WorkModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
