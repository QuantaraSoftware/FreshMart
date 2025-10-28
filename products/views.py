from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    categories = Category.objects.filter(is_active=True)
    featured_products = Product.objects.filter(is_active=True, is_featured=True)
    return render(request, 'home.html', {'categories': categories, 'featured_products': featured_products})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'products/product_detail.html', {'product': product})
