from django.urls import path
from shop.views import base, product_detail
from django.conf.urls.static import static
from django.conf import settings

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('catalog/<int:pk>', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
