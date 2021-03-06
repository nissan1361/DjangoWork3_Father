
from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'магазин'

    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')

