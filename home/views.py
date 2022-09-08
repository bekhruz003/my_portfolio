from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView
from .models import HomeModel, AboutModel, WorkModel, ContactModel
from .forms import ContactForm
from .utils import send_bot_message


# from django.core.mail import send_mail
# from django.conf.global_settings import EMAIL_HOST_USER


# class HomeView(ListView):
#     template_name = 'index.html'
#     model = HomeModel
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         data = super().get_context_data()
#         data['abouts'] = AboutModel.objects.all()
#         data['works'] = WorkModel.objects.all()
#         return data


class ContactView(CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('home')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        # message = f"Здравствуйте {form.instance.name} ! ваше сообщение получено."
        # send_mail("Мы свяжемся с вами.", message, EMAIL_HOST_USER, [form.instance.email])
        send_bot_message(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['home'] = HomeModel.objects.all()
        data['abouts'] = AboutModel.objects.all()
        data['works'] = WorkModel.objects.all()
        return data
