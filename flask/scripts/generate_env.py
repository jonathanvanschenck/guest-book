# This generates the .env file for the flask app

import uuid
from sys import argv

config = {
    "FLASK_APP":"wsgi.py"
}

try:
    value = argv[1]
except IndexError:
    value = "dev"

if value.lower()[0] == "p":
    config.update({"DATABASE_URL":"postgresql://flask_user:flask_password@db:5432/flask_db"})


with open(".env","w") as f:
    f.write("SECRET_KEY="+str(uuid.uuid4().hex)+"\n")
    for k,v in config.items():
        f.write(k+"="+v+"\n")
