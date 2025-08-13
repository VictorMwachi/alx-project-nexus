# EasyBuy: A Robust E-commerce API

**A backend foundation for modern online retail.**

---

## 📖 Overview

**EasyBuy** is a powerful and scalable backend API built with **Django** and **Django REST Framework (DRF)**, designed to provide all the essential server-side functionality needed to power a modern e-commerce web or mobile application.

It focuses on:

* **Security** — Robust authentication & secure data handling.
* **Simplicity** — RESTful, intuitive endpoints for easy frontend integration.
* **Scalability** — Industry-standard tools and best practices for growth.

---

## 🛠 Technology Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Backend Framework | Django                |
| API Layer         | Django REST Framework |
| Database          | PostgreSQL            |
| Authentication    | DRF Simple JWT        |

---

## 🏗 System Architecture

The system models core e-commerce concepts with Django ORM managing relationships.

**Core Models:**

* **User** — Authentication & profile data.
* **Product** — Name, description, price, stock.
* **Cart & Wishlist** — Temporary storage before purchase.
* **Order & OrderItem** — Purchase records linked to products.

**Simplified Relationship Diagram:**

```
User --< Order >-- OrderItem --< Product
```

---

## 🔐 Authentication Flow

Authentication is handled securely with **JSON Web Tokens (JWT)**.

**Steps:**

1. **Login:** POST credentials to `/api/token/`
2. **Validation:** Server checks user credentials
3. **Token Issuance:** Returns Access & Refresh tokens
4. **Authorized Requests:** Include Access token in headers
5. **Token Refresh:** Use Refresh token when Access token expires

## 📡 API Endpoints

### **Authentication**

* `POST /api/users/register/` — Create a new account
* `POST /api/users/login/` — Log into your account
* `POST /api/users/token/verify/` — Verify JWT token
* `POST /api/users/token/refresh/` — Refresh JWT token
* `POST /api/users/logout/` — Log out of your account
* `GET /api/users/profile/` — Retrieve user profile

---

### **Products**

* `GET /api/products/items/` — List all products
* `GET /api/products/items/{id}` — Get product details by ID
* `GET /api/products/variants/` — List product variants

---

### **Sales** *(Auth Required)*

#### **Wishlist**

* `GET /api/sales/wishlist/` — View wishlist

#### **Cart Management**

* `GET /api/sales/cart/` — View current cart
* `POST /api/sales/cart/add/` — Add item to cart
* `DELETE /api/sales/cart/remove/{item_id}/` — Remove item from cart
* `DELETE /api/sales/cart/clear/` — Clear all cart items

#### **Checkout**

* `POST /api/sales/checkout/` — Proceed to checkout


## 🚧 Challenges & Solutions

**1. Granular Permissions**

* **Problem:** Open product viewing, restricted ordering, admin-only product creation.
* **Solution:** DRF permissions (`AllowAny`, `IsAuthenticated`, `IsAdminUser`).

**2. Atomic Order Creation**

* **Problem:** Multiple steps must succeed or roll back.
* **Solution:** Wrap logic in `transaction.atomic()`.

---

## 🚀 Future Plans

**Phase 1:**

* React/Vue frontend
* Stripe payment integration
* Advanced product search

**Phase 2:**

* Celery & Redis for async tasks
* Product reviews & ratings
* Docker + AWS/Heroku deployment
