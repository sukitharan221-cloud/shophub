# This app deliberately has NO database models.
#
# For a beginner-friendly shopping cart, we store cart contents in the
# user's SESSION (a small piece of data Django keeps per-visitor,
# normally backed by a cookie + the database sessions table).
#
# Benefits of this approach:
#   - Works even for visitors who are NOT logged in
#   - No extra tables/migrations to manage for "cart items"
#   - Very easy to understand: the cart is just a Python dictionary
#
# See cart/cart.py for the actual Cart class that reads/writes the session.
