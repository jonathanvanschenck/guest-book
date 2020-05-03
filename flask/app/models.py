# This file manages the python-side of the database and it's objects

from time import time

from app import db

def current_processor_time():
    return int(time())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    message = db.Column(db.String(256))
    timestamp = db.Column(db.Integer, default=current_processor_time)

    def __repr__(self):
        return "<Post {0} | by: {1}>".format(self.id,self.name)

    def to_json(self,skip_animate = False):
        return {
            "name":self.name,
            "message":self.message,
            "timedelta":current_processor_time()-self.timestamp,
            "skip_animate":skip_animate
        }
