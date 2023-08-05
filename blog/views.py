from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogModel


class BlogListView(ListView):
    template_name = 'pages/blog.html'
    model = BlogModel
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'pages/blog-details.html'
    model = BlogModel
    context_object_name = 'blog'
