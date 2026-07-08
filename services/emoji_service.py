from services.emoji_buffer import emoji_buffer 
from sockets.emitter import update_display 

def add_emoji(emoji): 

    emoji_buffer.add(emoji) 
    update_display() 

def clear(): 

    emoji_buffer.clear() 
    update_display() 

def undo(): 

    emoji_buffer.undo() 
    update_display() 
    