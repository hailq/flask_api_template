#!/bin/bash

# Can setup app deployment here

exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - wsgi:app
