#!/bin/sh
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn records_project.wsgi