#!/bin/bash

# This is the entrypoint for the web server, it waits to make sure the
#  db is running, then ensure the db is up to date, then runs the webserver

echo "Waiting for PostgreSQL..."

# Wait unitl the postgres server is spun up
python scripts/wait.py

echo "PostgreSQL started"

# Configure and upgrade db
flask db migrate -m "setup"
flask db upgrade

# Launch web server
#  Note: gunicorn needs to run on the "external" port, so that it is accessible
#  to nginx, which is in a different container. But, we are still safe from
#  totally external attacks, becuase port 8000 is only 'exposed' (i.e. accessible
#  to other containers), not set as a fully external port.
gunicorn wsgi --worker-class eventlet --bind 0.0.0.0:8000
