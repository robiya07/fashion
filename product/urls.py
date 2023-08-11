from django.urls import path

from product.views import ShopView

app_name = 'product'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
]
