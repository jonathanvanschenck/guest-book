rm -r migrations
rm app.db

flask db init
flask db migrate -m "setup"
flask db upgrade
