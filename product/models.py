from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


class CategoryModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    slug = models.SlugField(verbose_name=_('slug'), max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        while self.__class__.objects.filter(slug=self.slug).exists():
            slug = self.__class__.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.name:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class TagModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    slug = models.SlugField(verbose_name=_('slug'), max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        while self.__class__.objects.filter(slug=self.slug).exists():
            slug = self.__class__.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.name:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tags'


class SizeModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'
        db_table = 'sizes'


class ColorModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=7)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        db_table = 'colors'


class CollectionModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        db_table = 'collections'


class ProductModel(models.Model):
    main_image = models.ImageField(verbose_name=_('main_image'), upload_to='images/products/main/')
    name = models.CharField(verbose_name=_('name'), max_length=200)
    short_description = models.CharField(verbose_name=_('short_description'), max_length=255)
    description = RichTextField(verbose_name=_('description'))
    real_price = models.DecimalField(verbose_name=_('real_price'), max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(verbose_name=_('price'), max_digits=10, decimal_places=2)
    sale_percent = models.PositiveSmallIntegerField(verbose_name=_('sale_percent'), default=0)
    created_at = models.DateTimeField(verbose_name=_('created_at'), auto_now_add=True)
    sku = models.PositiveIntegerField(verbose_name=_('sku'), unique=True)
    category = models.ForeignKey(verbose_name=_('category'), to=CategoryModel, on_delete=models.CASCADE,
                                 related_name='products')
    tags = models.ManyToManyField(verbose_name=_('tags'), to=TagModel, related_name='products')
    sizes = models.ManyToManyField(verbose_name=_('sizes'), to=SizeModel, related_name='products')
    colors = models.ManyToManyField(verbose_name=_('colors'), to=ColorModel, related_name='products')
    slug = models.SlugField(verbose_name=_('slug'), max_length=130, unique=True, blank=True, null=True)
    collection = models.ForeignKey(verbose_name=_('collection'), to=CollectionModel, related_name='products',
                                   on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        while self.__class__.objects.filter(slug=self.slug).exists():
            slug = self.__class__.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.name:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

    def is_new(self):
        current = datetime.now()
        days = current - timedelta(days=3)
        print(current, days)
        if self.created_at.date() >= days.date():
            return True
        return False

    @property
    def is_sale(self) -> bool:
        if self.sale_percent:
            return True
        return False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'
        ordering = ['-created_at']
