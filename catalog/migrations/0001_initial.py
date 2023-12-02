# Generated by Django 4.2.7 on 2023-12-02 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='product_img/', verbose_name='product preview')),
                ('price', models.FloatField(verbose_name='price per unit')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='last Modified')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]