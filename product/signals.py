from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import ProductModel


@receiver(post_save, sender=ProductModel)
def sale(sender, instance, created, **kwargs):
    if instance.sale_percent:
        instance.real_price = instance.price - (instance.price * instance.sale_percent) / 100
    else:
        instance.real_price = instance.price

    return instance