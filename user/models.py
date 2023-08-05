from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    country = models.CharField(verbose_name=_('country'), max_length=200, blank=True, null=True)
    address = models.CharField(verbose_name=_('address'), max_length=255, blank=True, null=True)
    city = models.CharField(verbose_name=_('city'), max_length=100, blank=True, null=True)
    region = models.CharField(verbose_name=_('region'), max_length=100, blank=True, null=True)
    zip_code = models.CharField(verbose_name=_('zip_code'), max_length=6, blank=True, null=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=13, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'