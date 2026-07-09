from .cart import Cart


def cart_summary(request):
    """
    A context processor runs on every single request and its return
    value is added to every template's context automatically.

    This lets us show the number of items in the cart on the navbar
    icon on EVERY page, without repeating code in every view.
    """
    cart = Cart(request)
    return {
        'cart_item_count': len(cart),
        'cart_total_price': cart.get_total_price(),
    }
