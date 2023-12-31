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
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last_name')),
                ('image', models.ImageField(upload_to='images/authors/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', ckeditor.fields.RichTextField(verbose_name='text')),
                ('image', models.ImageField(upload_to='images/blog/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True, verbose_name='slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.authormodel', verbose_name='author')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'db_table': 'blogs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Blog Tag',
                'verbose_name_plural': 'Blog Tags',
                'db_table': 'blog_tags',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogmodel', verbose_name='blog')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', to='blog.blogtagmodel', verbose_name='tags'),
        ),
    ]
