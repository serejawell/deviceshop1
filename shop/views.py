from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from shop.models import Product, Category


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'brand', 'category', 'price')
    success_url = reverse_lazy('shop:product_list')


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = queryset.filter(category__pk=category_id)
        return queryset

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'brand', 'price')

    def get_success_url(self):
        return reverse('shop:product_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid:
            new_post = form.save()
            new_post.slug = slugify(new_post.name)
            new_post.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:product_list')


