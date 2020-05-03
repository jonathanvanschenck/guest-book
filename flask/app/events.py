# This manages the python-side of the socket.io websocket server
from flask import copy_current_request_context
from flask_socketio import emit, disconnect

from app import socketio, db
from app.models import Post

@socketio.on('connect')
def on_connect():
    emit('log_to_console',{'data': 'Connected to server!'})
    return emit(
        'render_post_list',
        {
            'post_list':[p.to_json(skip_animate=True)\
                         for p in Post.query.all()]
        }
    )

@socketio.on('disconnect_request')
def on_disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()
    return emit('log_to_console',
                {'data': 'Disconnected from server!'},
                callback=can_disconnect)

@socketio.on('broadcast_post')
def on_broadcast_post(msg):
    new_post = Post(name=msg['name'],
                    message=msg['message'])
    db.session.add(new_post)
    db.session.commit()
    return emit('render_post', new_post.to_json(), broadcast=True)
