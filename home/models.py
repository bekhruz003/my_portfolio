from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class HomeModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    full_name = models.CharField(max_length=100, verbose_name=_('full name'))
    contact = models.CharField(max_length=100, verbose_name=_('contact'))
    about = models.CharField(max_length=100, verbose_name=_('about'))
    banner_image = models.ImageField(upload_to='banner/', verbose_name=_('banner image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'homies'


class AboutModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = RichTextUploadingField(verbose_name=_('description'))
    main_image = models.ImageField(upload_to='main/', verbose_name=_('main image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


class WorkModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    work_image = models.ImageField(upload_to='works/', verbose_name=_('work image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'


class ContactModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=255, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
