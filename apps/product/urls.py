from django.urls import path
from .views import detail_product, category

urlpatterns = [
    path('<slug:category_slug>', category , name='category'),
    path('<slug:category_slug>/<slug:product_slug>', detail_product , name='detail_product'),
]