from django.shortcuts import render
from products.models import Product, Review, Category
from templates import *
# Create your views here.

from django.shortcuts import HttpResponse, redirect
from datetime import datetime


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            "products": Product.objects.all()
        }
        return render(request, 'products/products.html', context=context)


def products_detail_view(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)
        comments = Review.objects.filter(products=products)

    context = {
        'product': products,
        'comments' : comments
    }
    return render(request, 'products/detail.html', context=context)

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request,'categories/index.html', context=context)
