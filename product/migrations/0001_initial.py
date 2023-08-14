# Generated by Django 4.2.4 on 2023-08-11 14:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CollectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
                'db_table': 'collections',
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='images/products/main/', verbose_name='main_image')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('short_description', models.CharField(max_length=255, verbose_name='short_description')),
                ('description', ckeditor.fields.RichTextField(verbose_name='description')),
                ('real_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='real_price')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('sale_percent', models.PositiveSmallIntegerField(default=0, verbose_name='sale_percent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('sku', models.PositiveIntegerField(unique=True, verbose_name='sku')),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True, verbose_name='slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.categorymodel', verbose_name='category')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.collectionmodel', verbose_name='collection')),
                ('colors', models.ManyToManyField(related_name='products', to='product.colormodel', verbose_name='colors')),
                ('sizes', models.ManyToManyField(related_name='products', to='product.sizemodel', verbose_name='sizes')),
                ('tags', models.ManyToManyField(related_name='products', to='product.tagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]
