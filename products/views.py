from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def home(request):
    """
    The Home Page.
    Shows: a hero banner (in the template), featured products,
    all categories, and the latest products.
    """
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    latest_products = Product.objects.filter(is_active=True)[:8]

    context = {
        'categories': categories,
        'featured_products': featured_products,
        'latest_products': latest_products,
    }
    return render(request, 'home.html', context)


def product_list(request, category_slug=None):
    """
    Shows every active product, optionally filtered by category,
    with simple keyword search and pagination.
    """
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Simple search: ?q=phone
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Pagination: show 8 products per page
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'category': category,
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'query': query or '',
    }
    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """
    Shows full details for a single product.
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)
