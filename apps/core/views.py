from itertools import product
from django.shortcuts import render
from apps.product.models import Product
# Create your views here.

def index(request):

    products = Product.objects.all()[0:8] # trae los objetos pero solo 8
    ctx = {
        "products": products
    }

    return render(request, 'core/index.html', ctx)

