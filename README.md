# guest-book
A simple web app that allows party guests to sign in

Well, in reality, this is a recipe for using `flask`, `postgres` and `nginx`
inside `docker` containers


# Running (using docker-compose)
```bash
 $ docker-compose build
 $ docker-compose up
```
After you are done, kill the containers:
```bash
 $ docker-compose down
```

# Development
## Set up
```bash
 $ cd flask
 $ python3 -m venv venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
 (venv) $ python scripts/generate_env.py
 (venv) $ ./scripts/generate_database.sh
```

## Running
Test server
```bash
 (venv) $ python wsgi.py
```
Development ready server (slower startups, worse logging and no debug mode, but
more accurate performance)
```bash
 (venv) $ gunicorn wsgi --worker-class eventlet --bind localhost:8000  
```

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
 - [ ] Configure nginx container
 - [ ] Modify flask to allow for postgres DB
 - [ ] Configure prostgres container
## Step 3 - Make is Pretty
 - [ ] Use bootstrap to make it look not awful
 - [ ] Add error checking in the submit form
 - [ ] Add user feedback about server connection status
 - [ ] Flesh out the README
