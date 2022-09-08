from django.contrib import admin
from .models import HomeModel, AboutModel, WorkModel
from modeltranslation.admin import TranslationAdmin


@admin.register(HomeModel)
class HomeModelAdmin(TranslationAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']


@admin.register(AboutModel)
class AboutModelAdmin(TranslationAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(WorkModel)
class WorkModelAdmin(TranslationAdmin):
    list_display = ['title']
    list_display_links = ['title']


class Media:
    js = (
        'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        'modeltranslation/js/tabbed_translation_fields.js',
    )
    css = {
        'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    }
