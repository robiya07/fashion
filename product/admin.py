from django.contrib import admin

from product.models import ProductModel, TagModel, SizeModel, ColorModel, CategoryModel


# Register your models here.
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price')


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
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
