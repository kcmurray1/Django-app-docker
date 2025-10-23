#!/bin/bash

sleep 10

# Create Database tables
python manage.py makemigrations peopleapp

python manage.py migrate

# Run the Django application
python manage.py runserver 0.0.0.0:8000 