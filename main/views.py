from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from main.models import ContactModel


# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'


class CreteContactView(CreateView):
    template_name = 'pages/contact.html'
    model = ContactModel
    fields = ('name', 'email', 'message')

    def get_success_url(self):
        return redirect('main:contact')
