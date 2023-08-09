from django.contrib import admin

from blog.models import BlogModel, BlogTagModel, AuthorModel, CommentModel


# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title', 'author')
    list_filter = ('created_at',)
    search_fields = ('title', 'author')
    readonly_fields = ('slug',)


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    readonly_fields = ('slug',)


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'blog')
    list_display_links = ('id', 'name', 'email', 'blog')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'blog')
