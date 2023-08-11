from django.contrib import admin

from main.models import MemberModel, ContactModel


# Register your models here.
@admin.register(MemberModel)
class MemberModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position')
    list_display_links = ('first_name', 'last_name', 'position')
    search_fields = ('first_name', 'last_name', 'position')


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')
