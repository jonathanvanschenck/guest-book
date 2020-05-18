# This script will ping the db, waiting until the db is fully spun up

import socket
import time
import os

host = os.environ.get("SQL_HOST") # "db"
port = int(os.environ.get("SQL_PORT")) # 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    # Attempt to connect to the db's port (this will only
    #  work if the db is functional)
    try:
        s.connect((host, port))
        s.close()
        break
    except socket.error as ex:
        # print((host, port))
        time.sleep(1.0)
