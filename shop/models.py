from datetime import datetime
from django.db import models


class Brand(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="наименование продукта",
        help_text="введите наименование продукта",
    )

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ["name", ]

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="наименование",
        help_text="введите наименование категории",
    )
    description = models.CharField(
        max_length=200, verbose_name="описание", help_text="введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="наименование продукта",
        help_text="введите наименование продукта",
    )
    brand = models.ForeignKey(Brand,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name="бренд",
                              help_text="введите название бренда",
                              related_name="product",
                              )
    description = models.CharField(
        max_length=150,
        verbose_name="описание",
        help_text="опишите продукта",
        blank=True,
        null=True,
    )
    description_full = models.TextField(
        verbose_name='полное описание',
        blank=True,
        null=True,
        help_text='введите полное описание продукта'
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        help_text="загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="категория",
        help_text="введите название категории",
        related_name="product",
    )
    price = models.IntegerField(
        verbose_name="стоимость", help_text="стоимость продукта"
    )
    created_at = models.DateField(default=datetime.now, verbose_name="дата создания")
    updated_at = models.DateField(default=datetime.now, verbose_name="дата редактирования")
    views_counter = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]

    def __str__(self):
        return f"{self.brand.name} {self.name}"
