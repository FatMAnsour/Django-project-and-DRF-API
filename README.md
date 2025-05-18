Product Search API

This is a Django REST Framework (DRF) project that provides an API for searching products with support for mixed-language queries (English and Arabic), partial keywords, and misspellings. The project uses PostgreSQL for full-text search capabilities.

Setup Instructions

Follow these steps to set up the project locally:





Clone the Repository
Clone the project to your local machine:

git clone <repository-url>
cd <repository-name>



Set Up a Virtual Environment
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install Dependencies
Install the required packages using the requirements.txt file (ensure you have PostgreSQL and django-debug-toolbar installed):

pip install -r requirements.txt

Note: Ensure your requirements.txt includes:

django>=4.0
djangorestframework>=3.14
psycopg2-binary>=2.9
django-debug-toolbar>=4.0



Set Up PostgreSQL Database





Install PostgreSQL if not already installed.



Create a database for the project:

psql -U postgres
CREATE DATABASE product_search_db;



Update your product_search/settings.py with the database configuration:

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



Add searchapp to INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    ...
    'searchapp',
    'django.contrib.postgres',
    'debug_toolbar',
]



Configure DEBUG_TOOLBAR in settings.py (optional, for debugging):

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']



Run Migrations
Apply the database migrations to create the necessary tables:

python manage.py makemigrations
python manage.py migrate



Create a Superuser (Optional)
Create a superuser to access the Django admin panel:

python manage.py createsuperuser



Run the Development Server
Start the Django development server:

python manage.py runserver

The API will be available at http://localhost:8000, and the admin panel at http://localhost:8000/admin/. The debug toolbar will also be accessible if configured.

API Documentation

Endpoint: Product Search





URL: /search/



Method: GET



Description: Search for products by query, with optional filters for category and brand. This endpoint is defined in searchapp/urls.py and included in the project’s root urls.py.



Query Parameters:





q (required): The search query (e.g., apple or misspellings like appl).



category (optional): Filter by category name (case-insensitive, e.g., fruit).



brand (optional): Filter by brand name (case-insensitive, e.g., nestle).



page (optional): Page number for pagination (default: 1).



page_size (optional): Number of results per page (default: 10, max: 100).

Example API Usage





Search for products with the query "apple"
Request:

GET http://localhost:8000/search/?q=apple

Response:

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



Search for products with the query "choco" in the category "snacks"
Request:

GET http://localhost:8000/search/?q=choco&category=snacks

Response:

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



Search with an empty query (Error Case)
Request:

GET http://localhost:8000/search/

Response:

{
    "error": "Please enter a search query"
}

Notes





The API supports pagination. Use the next and previous links in the response to navigate through results.



The search is optimized for partial keywords, misspellings, and mixed-language queries (English and Arabic) using PostgreSQL’s full-text search and trigram similarity.



The django-debug-toolbar is included for development purposes (accessible at http://localhost:8000/__debug__/) to monitor query performance.



Ensure you populate the Product, Brand, and Category models with data (e.g., via the admin panel or a script) to see search results.