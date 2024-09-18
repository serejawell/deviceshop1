from django.urls import path
from shop.views import base, product_detail, keyboards,mousepads,mouses,headsets
from django.conf.urls.static import static
from django.conf import settings

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
                  path('', base, name='base'),
                  path('catalog/<int:pk>', product_detail, name='product_detail'),
                  path('catalog/keyboards', keyboards, name='keyboards'),
                  path('catalog/mouses', mouses, name='mouses'),
                  path('catalog/mousepads', mousepads, name='mousepads'),
                  path('catalog/headsets', headsets, name='headsets'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
