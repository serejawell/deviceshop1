# Generated by Django 5.1.1 on 2024-09-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_views_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_full',
            field=models.TextField(blank=True, help_text='введите полное описание продукта', null=True, verbose_name='полное описание'),
        ),
    ]
