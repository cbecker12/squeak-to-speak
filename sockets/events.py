from flask import request 
from flask_socketio import emit 

from app import socketio 


@socketio.on("connect") 
def on_connect(): 
    print(f"Connected: {request.sid}") 

@socketio.on("disconnect") 
def on_disconnect(): 
    print(f"Disconnected: {request.sid}") 
