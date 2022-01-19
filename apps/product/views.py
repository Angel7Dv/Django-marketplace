from django.shortcuts import render, get_object_or_404
from .models import Product, Category
import random

# Create your views here.

def detail_product(request, category_slug, product_slug):    
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
                                    # se accede a un parametro por doble __ category__slug
    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    ctx = {    
        'product': product,
        'similar_products': similar_products,
    }
    return render(request, 'core/detail_product.html', ctx)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug )
    ctx = {
        "category": category
    }
    return render(request, 'core/category.html', ctx)


