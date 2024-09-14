from django.shortcuts import render, get_object_or_404
from shop.models import Product, Category

# def base(request):
#     return render(request, 'base.html')

def base(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog.html',context)


# def product_detail(request, category_slug, product_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     product = get_object_or_404(Product, slug=product_slug, category=category)
#
#     # Ваш код для отображения деталей продукта
#     return render(request, 'product_detail.html', {'product': product})

def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
