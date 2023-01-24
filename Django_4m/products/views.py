from django.shortcuts import HttpResponse, redirect, render
from datetime import datetime

from Django_4m.products.models import Category, Product, Review_comm



def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request,'categories/index.html', context=context)

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def product_detail_view(request, id):
    if request.method == 'GET':

        product = Product.objects.get(id=id)
        comments = Review_comm.objects.filter(product=product)
        context = {
            'products': product,
            'comments': comments,

        }
        return render(request, 'products/detail.html', context=context)




def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id:
            products = Product.objects.filter(category=Category.objects.get(id=category_id))
        else:
            products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def greeting(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def date_(request):
    if request.method == 'GET':
        return HttpResponse(f'data{datetime.now().date()}')


def farewell(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')