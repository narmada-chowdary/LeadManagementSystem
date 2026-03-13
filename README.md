Installation Guide
Step 1: Install Python

Download and install Python 3.x.

Verify installation:

python --version
Step 2: Install Django

Open terminal and run:

pip install django

Verify installation:

django-admin --version
Step 3: Create the Project
django-admin startproject lead_management
cd lead_management

Step 4: Create App
python manage.py startapp leads

Add the app to settings.py:

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'leads',
]

Step 5: Create Database

Run migrations:

python manage.py makemigrations
python manage.py migrate

Step 6: Create Admin User
python manage.py createsuperuser

Login to admin panel:

http://127.0.0.1:8000/admin

Step 7: Run the Server

Start the development server:
python manage.py runserver

Open browser:

http://127.0.0.1:8000
