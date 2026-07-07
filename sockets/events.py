from flask import request 
#from flask_socketio import emit 
from extensions import socketio 
from services.emoji_buffer import emoji_buffer 
from sockets.emitter import update_display 
from shared.constants import * 

@socketio.on("connect") 
def connect(): 
    print(f"Connected: {request.sid}") 

@socketio.on("disconnect") 
def disconnect(): 
    print(f"Disconnected: {request.sid}") 

@socketio.on(ADD_EMOJI) 
def add_emoji(data): 
    emoji_buffer.add(data["emoji"]) 
    update_display() 

@socketio.on(CLEAR_DISPLAY) 
def clear_display(): 
    emoji_buffer.clear() 
    update_display() 

@socketio.on(UNDO) 
def undo(): 
    emoji_buffer.undo() 
    update_display() 
    