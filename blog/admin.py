from django.contrib import admin

from blog.models import BlogModel, BlogTagModel, AuthorModel, CommentModel


# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author')


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog')
    list_display_links = ('name', 'email', 'blog')
    search_fields = ('name', 'email', 'blog')
