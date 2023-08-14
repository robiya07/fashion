from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView

from blog.models import BlogModel
from main.models import ContactModel, MemberModel


# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['blogs'] = BlogModel.objects.all()[:3]
        return data


class CreteContactView(CreateView):
    template_name = 'pages/contact.html'
    model = ContactModel
    fields = ('name', 'email', 'message')

    def get_success_url(self):
        return redirect('main:contact')


class AboutView(ListView):
    template_name = 'pages/about.html'
    model = MemberModel
    context_object_name = 'members'
