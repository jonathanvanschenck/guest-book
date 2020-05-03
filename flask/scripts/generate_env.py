# This generates the .env file for the flask app

import uuid

with open(".env","w") as f:
    f.writ("FLASK_APP=wsgi.py\n")
    f.write("SECRET_KEY="+str(uuid.uuid4().hex)+"\n")
