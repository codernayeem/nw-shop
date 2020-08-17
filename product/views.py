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


def get_random_products(request):
    c = {}
    c['request_type'] = request.GET.get('type', 'html') # html, json
    c['multiple'] = request.GET.get('multiple', '1') # '1' : multiple, '0' : single
    c['category'] = request.GET.get('category', None)
    c['product_id'] = request.GET.get('product_id', None)
    c['limit'] = request.GET.get('limit', '10')
    c['random'] = request.GET.get('random', '1') # '1' : random, '0' : serialized

    if c['request_type'] in ['html', 'json'] and c['multiple'] in ['1', '0'] and c['random'] in ['1', '0']:

        c['multiple'] = True if c['multiple'] == '1' else False
        c['random'] = True if c['random'] == '1' else False
        
        if c['multiple']:
            try:
                c['products'] = Product.objects.all()
            except:
                c['products'] = []
            c['products_count'] = len(c['products'])

            return render(request, 'random_products.html', c)
