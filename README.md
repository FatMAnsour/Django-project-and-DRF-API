# **Product Search API**

A powerful and flexible API built using **Django REST Framework (DRF)**, designed to support advanced product search capabilities with:

- Multilingual query support (English and Arabic)
- Tolerance for partial keywords and misspellings
- Efficient full-text search using **PostgreSQL**

---

## 🚀 Features

- Full-text search powered by PostgreSQL
- Trigram similarity for fuzzy matching
- Case-insensitive filtering by category and brand
- Pagination support for scalable browsing
- Debugging tools integrated with `django-debug-toolbar`

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Make sure PostgreSQL is installed and accessible from the command line, then run:

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes:

```txt
django>=4.0
djangorestframework>=3.14
psycopg2-binary>=2.9
django-debug-toolbar>=4.0
```

---

## 🗄️ PostgreSQL Configuration

### 1. Install PostgreSQL

Download and install PostgreSQL from the official website:  
👉 https://www.postgresql.org/download/

After installation, make sure the PostgreSQL `bin` directory (e.g., `C:\Program Files\PostgreSQL\17\bin`) is added to your system's PATH.

### 2. Create a PostgreSQL Database

Open your terminal or command prompt and run:

```bash
psql -U postgres
```

Then within the PostgreSQL prompt:

```sql
CREATE DATABASE product_search_db;
\c product_search_db
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;
```

> Replace `postgres` with your PostgreSQL username if different.

---

### 3. Configure Django Settings

In `product_search/settings.py`, update the `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'product_search_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Add Required Django Apps

Ensure the following are included in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'searchapp',
    'django.contrib.postgres',
    'debug_toolbar',
]
```

### 5. (Optional) Configure Django Debug Toolbar

```python
if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']
```

---

## 🧱 Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## 🔄 Run the Development Server

```bash
python manage.py runserver
```

- API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin/
- Debug Toolbar: http://localhost:8000/__debug__/

---

## 📖 API Reference

### 🔍 Product Search Endpoint

- **URL**: `/search/`
- **Method**: `GET`
- **Description**: Search for products with optional filters for category and brand.

#### Query Parameters:

| Parameter   | Required | Description |
|-------------|----------|-------------|
| `q`         | ✅       | The search term (supports fuzzy and partial match) |
| `category`  | ❌       | Filter by category name (case-insensitive) |
| `brand`     | ❌       | Filter by brand name (case-insensitive) |
| `page`      | ❌       | Page number (default: 1) |
| `page_size` | ❌       | Results per page (default: 10, max: 100) |

---

## 🧪 Example Requests

### 1. Basic Search

```http
GET /search/?q=apple
```

```json
{
  "count": 25,
  "next": "http://localhost:8000/search/?q=apple&page=2",
  "previous": null,
  "results": [
    {
      "name": "Apple Juice",
      "brand": "Nestle",
      "category": "Beverages",
      "nutrition_facts": "Calories: 120, Sugar: 25g"
    },
    {
      "name": "Apple Pie",
      "brand": "BakeryCo",
      "category": "Desserts",
      "nutrition_facts": "Calories: 300, Fat: 15g"
    }
  ]
}
```

### 2. Filtered Search

```http
GET /search/?q=choco&category=snacks
```

```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "Chocolate Bar",
      "brand": "Mars",
      "category": "Snacks",
      "nutrition_facts": "Calories: 200, Sugar: 20g"
    }
  ]
}
```

### 3. Empty Query (Error Case)

```http
GET /search/
```

```json
{
  "error": "Please enter a search query"
}
```

---

## 📝 Notes

- Pagination is supported using `next` and `previous` URLs.
- Search supports misspellings, partial queries, and mixed languages (English and Arabic).
- Debug toolbar available at `/__debug__/` when in development mode.
- Populate `Product`, `Brand`, and `Category` models to view search results.
