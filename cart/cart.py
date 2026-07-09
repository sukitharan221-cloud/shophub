from decimal import Decimal
from django.conf import settings
from products.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    """
    A shopping cart stored in the request's session.

    The underlying data looks like this in the session:
        {
            "3": {"quantity": 2, "price": "19.99"},
            "7": {"quantity": 1, "price": "49.00"},
        }
    where each key is a Product's primary key (as a string, because
    session data is stored as JSON, and JSON dict keys must be strings).
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            # No cart yet for this visitor -> create an empty one
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """Add a product to the cart, or update its quantity."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        # Never let quantity go below 1 or above available stock
        self.cart[product_id]['quantity'] = max(1, self.cart[product_id]['quantity'])
        self.save()

    def save(self):
        # Tell Django the session has been modified, so it gets saved.
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the cart completely."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Loop over the items in the cart, attaching the actual Product
        object to each entry so templates can show name/image/etc.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_map = {str(p.id): p for p in products}

        cart = self.cart.copy()
        for product_id, item in cart.items():
            if product_id in products_map:
                item = item.copy()
                item['product'] = products_map[product_id]
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item

    def __len__(self):
        """Total number of individual items (sum of quantities)."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        """Empty the cart, e.g. after an order is placed."""
        del self.session[CART_SESSION_ID]
        self.save()
