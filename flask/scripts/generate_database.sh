#!/usr/bin/env bash

rm -r migrations
rm app.db

venv/bin/flask db init
venv/bin/flask db migrate -m "setup"
venv/bin/flask db upgrade
