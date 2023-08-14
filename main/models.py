from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import CollectionModel


class MemberModel(models.Model):
    first_name = models.CharField(verbose_name=_('first_name'), max_length=100)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=100)
    position = models.CharField(verbose_name=_('position'), max_length=100)
    image = models.ImageField(verbose_name=_('image'), upload_to='images/members/')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        db_table = 'members'


class ContactModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(verbose_name=_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        db_table = 'contacts'


class BannerModel(models.Model):
    collection = models.OneToOneField(verbose_name=_("collection"), to=CollectionModel, on_delete=models.CASCADE,
                                      related_name='banner')
    title = models.CharField(verbose_name=_("title"), max_length=60)
    description = models.TextField(verbose_name=_("description"))
    created_at = models.DateTimeField(verbose_name=_("created_at"), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_("is_active"), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        db_table = 'banners'
        ordering = ['created_at']
