<<<<<<< HEAD
# Inventory-Management-System
=======
<<<<<<< HEAD
# Inventory-Management-System
=======

This project is a Django-based Inventory Management System that provides a simple API for managing inventory items. It supports user authentication, CRUD operations for inventory items, and utilizes caching to optimize performance.

Features:
CRUD operations for inventory items (Create, Retrieve, Update, Delete).
Caching for inventory items using Redis to enhance performance.
User Authentication with registration and login features.
Comprehensive Logging for monitoring and debugging.
JWT Authentication for securing API endpoints.
Unit tests for models, serializers, and views.



Prerequisites:
Python 3.8+
Django 3.2+
PostgreSQL (or any other preferred database)
Redis (for caching)
pip (Python package manager)
Virtual Environment (recommended)


Step1: Clone the repository:

    git clone https://github.com/Meena-bandaru/Inventory-Management-System
    cd inventory-management-system

step2: Create a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

step3: Install the dependencies:

    pip install -r requirements.txt.

step4: Set up the PostgreSQL database:
    Ensure that PostgreSQL is installed and running on your machine
    download link: https://www.postgresql.org/download/

    Step 1: Open PostgreSQL Command Line

        step 1.Launch the PostgreSQL Command Line Interface (psql):
            On Windows, you can search for "SQL Shell (psql)" in your Start menu.
            On macOS or Linux, open your terminal and type psql to start the command line.

        Step 2: Connect to the PostgreSQL Server
        Connect to your PostgreSQL server:
        If prompted, enter your username (default is usually postgres) and password.
        You can also connect using the command:
        psql -U user_name

        Step 3: Create a New Database
        
            Once you are connected to the server, you can create a new database with the following command:
            CREATE DATABASE your_database_name;
            Replace your_database_name with your desired database name.
        Step 4: Grant all necessary permissions to user to perform actions on db
        
        step5: Upadte django settings file
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                        'NAME': 'db_name',
                        'USER': 'user_name',
                        'PASSWORD': 'password',
                        'HOST': 'localhost',
                        'PORT': '5432',
                    }
                }
step:5: Run redis server:
       Install redis server
        
step5: Apply migrations:

    python manage.py makemigrations
    python manage.py migrate
step6: Create a superuser:

    python manage.py createsuperuser

step7: Run the development server:

    python manage.py runserver
>>>>>>> d5837a8 (Initial commit)
>>>>>>> 85f7461 (Your commit message)
"# Inventory-Management-System" 
