from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm


@login_required
def checkout(request):
    """
    Shows billing details form + an order summary.
    On submit: creates the Order + OrderItems from the current cart,
    empties the cart, and shows a confirmation page.
    This demo only supports "Cash on Delivery" (no real payment gateway).
    """
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty. Add some products before checking out.')
        return redirect('products:product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.payment_method = 'cod'
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
                # Reduce stock to reflect the purchase
                product = item['product']
                product.stock = max(0, product.stock - item['quantity'])
                product.save()

            cart.clear()
            messages.success(request, 'Your order was placed successfully! Pay cash on delivery.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        # Pre-fill the form with the user's saved profile info, if any
        initial = {
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'phone': getattr(request.user.profile, 'phone', ''),
            'address': getattr(request.user.profile, 'address', ''),
            'city': getattr(request.user.profile, 'city', ''),
        }
        form = OrderCreateForm(initial=initial)

    return render(request, 'orders/checkout.html', {'form': form, 'cart': cart})


@login_required
def order_history(request):
    """List of all past orders for the logged-in user."""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Full details (items + totals + shipping info) for one order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
