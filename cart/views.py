from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """Add a product to the cart (or update its quantity)."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request, f'"{product.name}" was added to your cart.')
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Remove a product from the cart entirely."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f'"{product.name}" was removed from your cart.')
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Show everything currently in the cart, with quantity-update forms."""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True}
        )
    return render(request, 'cart/cart.html', {'cart': cart})
