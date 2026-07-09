from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishlistItem(models.Model):
    """
    Links a User to a Product they want to save for later.
    unique_together stops the same product being added twice for one user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-added_at']

    def __str__(self):
        return f'{self.user.username} \u2764 {self.product.name}'
