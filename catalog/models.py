from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    description = models.TextField(verbose_name='description', **NULLABLE)
    preview = models.ImageField(upload_to='product_img/', verbose_name='product preview', **NULLABLE)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    price = models.FloatField(verbose_name='price per unit')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='created')
    change_date = models.DateTimeField(auto_now=True, verbose_name='last Modified')

    def __str__(self):
        return f'{self.name}, {self.category}, price = {self.price})'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    description = models.TextField(verbose_name='description', **NULLABLE)
    # created_at = models.DateTimeField(auto_now=True, verbose_name='created')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug = models.CharField(max_length=80, verbose_name='slug')
    content = models.TextField(verbose_name='content')
    preview = models.ImageField(upload_to='blog_img/', verbose_name='post preview', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    is_published = models.BooleanField(verbose_name='published')
    view_count = models.IntegerField(verbose_name='view count', default='0')

    def __str__(self):
        return f'{self.title}, views: {self.view_count}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
