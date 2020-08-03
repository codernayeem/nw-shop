from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from .models import Category, Product


def categories_view(request):
    categories = Category.objects.all()

    return render(request, 'categories.html', {'categories': categories})


def category_view(request, category):
    try:
        category = Category.objects.get(name=category)
    except:
        category = None
    if category:
        products = Product.objects.filter(category=category)
        return render(request, 'products.html', {'category': category, 'products': products})
    else:
        return HttpResponseNotFound()


def product_details_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        product = None
    if product:
        c = {'product': product}
    else:
        c = {'errorId': True}

    return render(request, 'product_details.html', c)
