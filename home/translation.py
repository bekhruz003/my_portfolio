from modeltranslation.translator import register, TranslationOptions
from .models import HomeModel, AboutModel, WorkModel


@register(HomeModel)
class HomeModelTranslation(TranslationOptions):
    fields = ('title', 'full_name', 'contact', 'about')


@register(AboutModel)
class AboutModelTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(WorkModel)
class WorkModelTranslation(TranslationOptions):
    fields = ('title', 'body')
