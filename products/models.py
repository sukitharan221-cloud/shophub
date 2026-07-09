from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# ==========================
# Category Model
# ==========================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "products:product_list_by_category",
            args=[self.slug]
        )


# ==========================
# Product Model
# ==========================
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField(blank=True)

    sku = models.CharField(
        max_length=100,
        unique=True
    )

    brand = models.CharField(
        max_length=100,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(default=0)

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False,
        help_text="Featured products are highlighted on the home page."
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this product from the shop without deleting it."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "products:product_detail",
            args=[self.slug]
        )

    @property
    def in_stock(self):
        return self.stock > 0