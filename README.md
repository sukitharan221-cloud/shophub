<<<<<<< HEAD
# ShopHub — Django eCommerce Demo

A simple, beginner-friendly eCommerce website built with Django, SQLite,
Bootstrap 5 and vanilla JavaScript.

## Features
- Home page: hero banner, categories, featured products, latest products
- Accounts: register, login, logout, profile (with order history)
- Products: list, category filter, search, pagination, detail page
- Cart: session-based add / remove / update quantity / total
- Wishlist: add / remove (requires login)
- Checkout: billing form + order summary + Cash on Delivery (demo)
- Orders: order history + order detail
- Full Django admin for managing products, categories, orders, users

## 1. Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations (creates db.sqlite3 and all tables)
python manage.py makemigrations
python manage.py migrate

# 4. Create an admin (superuser) account
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.
Open http://127.0.0.1:8000/admin/ and log in with your superuser account
to add Categories and Products — the site will look empty until you do!

## 2. Adding your first products

1. Go to `/admin/`
2. Click **Categories** → **Add Category** → enter a name (e.g. "Electronics") → Save
3. Click **Products** → **Add Product** → fill in name, category, price,
   description, upload an image, set stock, check "Is featured" for a few → Save
4. Visit the home page — your products will now appear!

## 3. Project Structure

```
shophub/
│── manage.py
│── requirements.txt
│── shophub/            # Project settings, root urls.py, wsgi/asgi
│── accounts/           # Register, login, logout, profile (extends User with Profile model)
│── products/           # Category & Product models, listing/detail views
│── cart/                # Session-based shopping cart (no DB model needed)
│── wishlist/            # Per-user saved products
│── orders/              # Checkout, Order & OrderItem models, order history
│── templates/           # All HTML templates (shared, using template inheritance)
│── static/              # CSS & JavaScript
│── media/               # Uploaded product/category images & avatars (created at runtime)
```

## Notes for learners
- The cart does **not** need a database model — it's stored in the
  Django session (`cart/cart.py`). This is simpler for beginners and
  works even for users who aren't logged in.
- `accounts/models.py` uses a Django **signal** to automatically create
  a `Profile` for every new `User`.
- Checkout is a **Cash on Delivery demo only** — no real payment gateway
  is integrated.
- Run `python manage.py createsuperuser` any time you want another admin account.
=======
# shophub
>>>>>>> 0ee8e68c256354465a0041cf1c3e350bde1c2534
