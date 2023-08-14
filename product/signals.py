from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from product.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def sale(sender, instance, **kwargs):
    if instance.sale_percent:
        instance.real_price = instance.price - (instance.price * instance.sale_percent) / 100
    else:
        instance.real_price = instance.price

    return instance