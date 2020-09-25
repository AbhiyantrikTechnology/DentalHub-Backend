#!/bin/bash
# entry.sh
python manage.py makemigrations
python manage.py migrate
# gunicorn dental.wsgi:application --bind 0.0.0.0:8081
python manage.py runserver 0.0.0.0:8081
