"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import categories_view, category_view, product_details_view, get_random_products

urlpatterns = [
    path('categories/', categories_view, name='categories'),
    path('categories/<category>/', category_view, name='category_view'),
    path('view/<int:product_id>/', product_details_view, name='product_details_view'),
    path('get/random/', get_random_products, name='random_products_view'),
]
