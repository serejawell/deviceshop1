# Generated by Django 5.1.1 on 2024-09-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_brand_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_counter',
            field=models.PositiveIntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
