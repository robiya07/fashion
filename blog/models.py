from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class AuthorModel(models.Model):
    first_name = models.CharField(verbose_name=_('first_name'), max_length=100)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=100)
    image = models.ImageField(verbose_name=_('image'), upload_to='images/authors/')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        db_table = 'authors'


class BlogTagModel(models.Model):
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
        verbose_name = 'Blog Tag'
        verbose_name_plural = 'Blog Tags'
        db_table = 'blog_tags'


class BlogModel(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    text = RichTextField(verbose_name=_('text'))
    image = models.ImageField(verbose_name=_('image'), upload_to='images/blog/')
    author = models.ForeignKey(verbose_name=_('author'), to=AuthorModel, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(verbose_name=_('tags'), to=BlogTagModel, related_name='blogs')
    created_at = models.DateTimeField(verbose_name=_('created_at'), auto_now_add=True)
    slug = models.SlugField(verbose_name=_('slug'), max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        while self.__class__.objects.filter(slug=self.slug).exists():
            slug = self.__class__.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.title:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'blogs'
        ordering = ['-created_at']


class CommentModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(verbose_name=_('phone'), max_length=13)
    comment = models.TextField(verbose_name=_('comment'))
    blog = models.ForeignKey(verbose_name=_('blog'), to=BlogModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(verbose_name=_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'
        ordering = ['-created_at']
