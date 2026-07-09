from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from products.models import Product
from .models import WishlistItem


@login_required
def wishlist_detail(request):
    """Show every product the logged-in user has saved."""
    items = WishlistItem.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist/wishlist.html', {'items': items})


@login_required
@require_POST
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    obj, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f'"{product.name}" was added to your wishlist.')
    else:
        messages.info(request, f'"{product.name}" is already in your wishlist.')
    return redirect(request.META.get('HTTP_REFERER', 'wishlist:wishlist_detail'))


@login_required
@require_POST
def wishlist_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    messages.info(request, f'"{product.name}" was removed from your wishlist.')
    return redirect('wishlist:wishlist_detail')
