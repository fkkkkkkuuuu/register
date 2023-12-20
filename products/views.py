from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm



def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products/product_list.html', {'products': products})



def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
