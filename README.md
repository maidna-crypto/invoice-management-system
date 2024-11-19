# Invoice Management System

A Django-based system for managing invoices along with multiple invoice details. This project allows the creation and updating of invoices and invoice details.

## Features

- Create and manage invoices.
- Add and update invoice details.
- Ensure that each invoice has a unique invoice number.

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the repository:

```
git clone https://github.com/maidna-crypto/invoice-management-system.git
cd invoice-management-system
```

### 2. Set up a virtual environment:
It’s recommended to use a virtual environment to manage the project’s dependencies.

```
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3. Install dependencies:
Install the required Python packages using the requirements.txt file.

```
pip install -r requirements.txt
```

### 4. Configure Database:
The project is initially set up to use SQLite as the database. You can modify settings.py to use another database, such as PostgreSQL or MySQL, if required. Make sure to adjust the DATABASES settings in settings.py.

### 5. Apply migrations:
Run the Django migrations to create the necessary database tables.

```
python manage.py migrate
```

### 6. Create a superuser (optional):
To access the Django admin interface and manage invoices, create a superuser:

```
python manage.py createsuperuser
```

### 7. Run the development server:
Start the Django development server:
```
python manage.py runserver
```
The project will be accessible at http://127.0.0.1:8000/ in your browser.
