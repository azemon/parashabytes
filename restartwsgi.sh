#!/bin/bash

# kill existing WSGI server
kill $(ps x | gawk '$5 ~ /apache2/ {print $1}')

# clear the Python cache
find . -name '*.pyc' -delete

# update the static files
python3 manage.py collectstatic --noinput
