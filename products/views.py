from django.shortcuts import render, redirect
from products.models import Product, Review, Category
from products.forms import *




def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            "products": products
        }
        return render(request, 'products/products.html', context=context)


def products_detail_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        comments = Review.objects.filter(products=product)
        context = {
            'product': product,
            'comments' : comments
        }
        return render(request, 'products/detail.html', context=context)

    elif request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                post_id=product
            )
            return redirect(f'/products/{product.id}/')

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request,'categories/index.html', context=context)


def create_product_view(request):
    form = ProductCreateForm(data=request.POST)
    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'products/create.html', context=context)
    else:
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price')
            )
            return redirect('/products/')
