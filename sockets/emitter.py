from extensions import socketio 

from services.emoji_buffer import emoji_buffer 
from shared.constants import DISPLAY_UPDATE 

def update_display(): 

    socketio.emit( 
        DISPLAY_UPDATE, 
        { 
            "text": emoji_buffer.get_display_text() 
        }
    ) 
