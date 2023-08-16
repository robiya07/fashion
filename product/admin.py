from django.contrib import admin
from django.utils.safestring import mark_safe

from product.forms import ColorModelAdminForm
from product.models import ProductModel, TagModel, SizeModel, ColorModel, CategoryModel


# Register your models here.
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price')
    readonly_fields = ('real_price',)


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    form = ColorModelAdminForm
    list_display = ('name', 'color')
    list_display_links = ('name',)
    search_fields = ('name',)

    def color(self, obj):
        return mark_safe(
            f'<div style="width: 25px; height: 25px; border-radius: 50%; background-color: {obj.name};"></div>')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
