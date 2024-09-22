from django.urls import path

from shop.models import Category
from shop.views import ProductListView, ProductCreateView, ProductDetailView, ProductDeleteView, ProductUpdateView
from django.conf.urls.static import static
from django.conf import settings

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='product_list_by_category'),
]
