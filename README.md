# SnackShop - Django E-commerce Website for Selling Snacks

A simple, functional e-commerce site built with Django. Includes product catalog,
categories, session-based shopping cart, checkout/order creation, and Django admin
for managing products and orders.

## Features
- Product catalog with categories
- Product detail pages with images, price, stock
- Session-based shopping cart (add/update/remove items)
- Checkout flow that creates an Order + OrderItems
- Django admin panel for managing everything
- User registration/login (Django built-in auth)

## Project structure
```
snackshop/
├── manage.py
├── requirements.txt
├── snackshop/        # project settings/urls
├── store/             # products & categories app
├── cart/               # session-based cart app
├── orders/            # checkout & orders app
├── templates/         # HTML templates
├── static/            # CSS
└── media/             # uploaded product images
```

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```

4. Run the dev server:
   ```bash
   python manage.py runserver
   ```

5. Visit:
   - Store: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Adding products
Log into `/admin/`, create a **Category** (e.g. "Chips", "Chocolates", "Namkeen"),
then add **Products** under that category with a name, price, stock, description,
and image.

## Notes / next steps
- Payment gateway (Razorpay/Stripe) is not integrated — orders are created with
  status "pending" and you can wire a payment gateway inside `orders/views.py`.
- For production: set `DEBUG=False`, configure `ALLOWED_HOSTS`, use Postgres,
  serve static/media via whitenoise or S3, and set a real `SECRET_KEY` via env var.
