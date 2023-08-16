from django.shortcuts import render
from django.views.generic import ListView

from product.models import ProductModel


# Create your views here.
class ShopView(ListView):
    template_name = "pages/shop.html"
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = ProductModel.objects.all()
        return qs
