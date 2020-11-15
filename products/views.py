from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product
from .controller import ProductController


# Create your views here.
def products(request):
    product = ProductController.get_products()
    return render(request, 'products/products.html', {'products': product})

def addProd(request):
    product = ProductController.addProduct()
    return HttpResponse(product)