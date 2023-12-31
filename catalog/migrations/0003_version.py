# Generated by Django 4.2.7 on 2023-12-24 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=30, verbose_name='version number')),
                ('version_name', models.CharField(max_length=200, verbose_name='version name')),
                ('is_current', models.BooleanField(default=True, verbose_name='current version')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'version',
                'verbose_name_plural': 'versions',
            },
        ),
    ]
