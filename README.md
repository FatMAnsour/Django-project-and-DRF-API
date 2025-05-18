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

Follow the instructions below to set up the project locally.

### 1. Clone the Repository

```bash
git clone <https://github.com/FatMAnsour/Django-project-and-DRF-API.git>
cd <repository-name>

### 2. Set Up a Virtual Environment
![image](https://github.com/user-attachments/assets/c2be9202-5663-4286-b886-005e7d610530)
### 3. Install Dependencies
pip install -r requirements.txt

## Database Configuration
### 1. Install PostgreSQL
Download and install PostgreSQL from the official website:
👉 https://www.postgresql.org/download/
Make sure to note the installation directory (e.g., C:\Program Files\PostgreSQL\17\bin on Windows).
### 2. Create a PostgreSQL Database
Run the following commands in the terminal or using psql

![image](https://github.com/user-attachments/assets/7d180809-3cfc-46b0-84b0-51d56dd1c238)

### Then, within the PostgreSQL prompt:
![image](https://github.com/user-attachments/assets/ffc8cfeb-8bb2-48fb-be3d-b716bfd49b74)

### 3. Configure settings.py
Update the DATABASES section in product_search/settings.py

![image](https://github.com/user-attachments/assets/614be00e-03d4-4b8a-aff0-d6cfc670b58c)

### 4. Add Required Django Apps

![image](https://github.com/user-attachments/assets/6c52e99e-e197-433e-89da-662711a1ba98)

## Database Migrations

![image](https://github.com/user-attachments/assets/2e623105-a27b-40a1-969c-f2c3e098abd2)

## Run the Development Server
![image](https://github.com/user-attachments/assets/7801c9dc-3566-4a22-97d3-5dcd0def19d6)

##  API Reference

Product Search Endpoint
URL: /search/
Method: GET
Description: Search for products with optional filters for category and brand.

## Example Requests

GET /search/?q=apple

## Response:

![image](https://github.com/user-attachments/assets/f651a1bf-7cde-43a5-a979-97efce9786bc)



















