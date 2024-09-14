from django.contrib import admin

from shop.models import Category, Product,Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
    list_editable = ('name', 'price','category','description')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)