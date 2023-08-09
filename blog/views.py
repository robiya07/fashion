from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CreateCommentForm
from blog.models import BlogModel, CommentModel


class BlogListView(ListView):
    template_name = 'pages/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        qs = BlogModel.objects.all()
        tag = self.request.GET.get('tag', '')
        if tag:
            qs = BlogModel.objects.filter(tags__slug=tag)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['tag'] = self.request.GET.get('tag', '')
        return data


class CreateCommentView(CreateView):
    form_class = CreateCommentForm

    def form_valid(self, form):
        blog_slug = self.kwargs['slug']
        blog = BlogModel.objects.get(slug=blog_slug)
        form.instance.blog = blog
        form.save()
        return redirect('blog:blog_detail', slug=blog_slug)


class BlogDetailView(DetailView):
    template_name = 'pages/blog-details.html'
    model = BlogModel
    context_object_name = 'blog'
