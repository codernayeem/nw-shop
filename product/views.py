from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Category


def categories_view(request):
    categories = Category.objects.all()

    return render(request, 'categories.html', {'categories': categories})
