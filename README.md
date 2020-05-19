# guest-book
A simple web app that allows party guests to leave a message

Well, in reality, this is a recipe for using `flask`, `postgres` and `nginx`
inside `docker` containers. Because, seriously, this would be WAY easier to do
with a piece of paper and a pen.

Jokes aside, one can fork this final commit and change the relevant files
to suit one's own needs, or one could use the commit history of this to see
a step-by-step guide on how to build up such an application.

# Production (using docker-compose)
## Set Up
Running this application in production mode requires `docker-compose`, which
you can download for free, [instructions found here](https://docs.docker.com/compose/install/).

Once you have `docker-compose` installed, you can build the docker images with
this command:
```bash
 $ docker-compose build
```

## Running
To then run the actual `docker` containers, execute:
```bash
 $ docker-compose up
```
The app should then be visible at (http://localhost/), or if you know your
system's external ip address, you can access it on your network at that address.

## Clean Up
After you are done, kill the containers with:
```bash
 $ docker-compose down
```
If you are REALLY done, and want to wipe the database, then also run:
```bash
 $ docker volume prune
```
But, be careful, cause this will kill other docker container's databases too
if don't have then active when you run this command. Be smart.

# Development
## Set up
To set up a development version, you will need to create a virtual python
environment in the `flask` directory, activate it and pip install the
necessary packages:
```bash
 $ cd flask
 $ python3 -m venv venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
```

Next, you will need to generate a development `.env` file (this will create a
new secret key for your flask app, among other things):
```bash
 (venv) $ python scripts/generate_env.py development
```

Finally, you will need to initialize and setup a `sqlite3` database:
```bash
 (venv) $ ./scripts/generate_database.sh
```

## Running
To run the webserver, we will use `gunicorn`:
```bash
 (venv) $ gunicorn wsgi --worker-class eventlet --bind 0.0.0.0:8000  
```
The app should then be visible at (http://localhost:8000/)

Have fun!

# To Do
## Step 1 - It works
 - [x] Create file structure
 - [x] Get flask to run locally
 - [x] Get javascript to work
 - [x] Design Guest Book html page
 - [x] Design Guest Book local javascript
 - [x] Add socket.io support
 - [x] Add db support
## Step 2 - Dockerify
 - [x] Create flask Dockerfile
 - [x] Configure nginx container
 - [x] Modify flask to allow for postgres DB
 - [x] Configure postgres container
## Step 3 - Make is Pretty
 - [x] Use bootstrap to make it look not awful
 - [x] Add error checking in the submit form
 - [x] Add user feedback about server connection status
 - [x] Flesh out the README
