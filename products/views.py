from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    """ A view to all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products, }

    return render(request, 'products/products.html', context)