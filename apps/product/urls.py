from django.urls import path
from .views import detail_product, category, search

urlpatterns = [
    path('search', search, name='search'),
    path('<slug:category_slug>', category , name='category'),
    path('<slug:category_slug>/<slug:product_slug>', detail_product , name='detail_product'),
]