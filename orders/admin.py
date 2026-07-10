from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Lets an admin see/edit an order's line items right on the Order page."""
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'city', 'status', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    list_editable = ('status',)
    search_fields = ('full_name', 'email', 'phone')
    inlines = [OrderItemInline]
