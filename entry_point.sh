#!/bin/bash
export DJANGO_SETTINGS=$DJANGO_SETTINGS_MODULE
export DEFAULT_BIND=0.0.0.0:$PUBLISHED_PORT
export DEFAULT_WORKERS=6
python mutant/manage.py makemigrations --no-input
python mutant/manage.py migrate
gunicorn mutant.wsgi --env DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS}" --bind "${DEFAULT_BIND}" --workers=${DEFAULT_WORKERS} --log-level debug --chdir ./mutant
