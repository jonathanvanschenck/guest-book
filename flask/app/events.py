# This manages the python-side of the socket.io websocket server
from flask import copy_current_request_context
from flask_socketio import emit, disconnect

from app import socketio

@socketio.on('connect')
def on_connect():
    return emit('log_to_console',{'data': 'Connected to server!'})

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
    return emit('render_post', msg, broadcast=True)
