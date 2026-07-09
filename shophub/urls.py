"""
Root URL configuration for ShopHub.

Each app manages its own urls.py; here we just "include" them under a
prefix. This keeps things organized as the project grows.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page lives directly at the root of the site
    path('', product_views.home, name='home'),

    # Each app's URLs, "namespaced" so we can do things like
    # {% url 'accounts:login' %} or {% url 'cart:cart_detail' %}
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('orders/', include('orders.urls', namespace='orders')),
]

# During development (DEBUG=True), Django needs this to serve uploaded
# media files (like product images) directly. In production this is
# normally handled by your web server (nginx, etc.) instead.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
