from django.urls import path

from blog.views import BlogListView, BlogDetailView, CreateCommentView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<slug:slug>/comment/', CreateCommentView.as_view(), name='comment'),
]
