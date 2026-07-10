"""
Root URL configuration for ShopHub.

Each app manages its own urls.py; here we just "include" them under a
prefix. This keeps things organized as the project grows.
"""
from django.contrib import admin
import django.urls
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views

urlpatterns = [
    django.urls.path('admin/', admin.site.urls),

    # Home page lives directly at the root of the site
    django.urls.path('', product_views.home, name='home'),

    # Each app's URLs, "namespaced" so we can do things like
    # {% url 'accounts:login' %} or {% url 'cart:cart_detail' %}
    django.urls.path('accounts/', django.urls.include('accounts.urls', namespace='accounts')),
    django.urls.path('products/', django.urls.include('products.urls', namespace='products')),
    django.urls.path('cart/', django.urls.include('cart.urls', namespace='cart')),
    django.urls.path('wishlist/', django.urls.include('wishlist.urls', namespace='wishlist')),
    django.urls.path('orders/', django.urls.include('orders.urls', namespace='orders')),
]

# During development (DEBUG=True), Django needs this to serve uploaded
# media files (like product images) directly. In production this is
# normally handled by your web server (nginx, etc.) instead.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
