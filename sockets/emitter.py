from extensions import socketio 
from shared.state import ServerState 
from services.emoji_buffer import emoji_buffer 
from shared.constants import DISPLAY_UPDATE, UPDATE_ADMIN 
from config import PORT 

def update_display(): 

    socketio.emit( 
        DISPLAY_UPDATE, 
        { 
            "text": emoji_buffer.get_display_text() 
        }
    ) 

def update_admin(): 

    print(
        {
        "keyboard_running": ServerState.keyboard_running,
        "display_clients": ServerState.display_clients,
        "control_clients": ServerState.control_clients,
        "last_key": ServerState.last_key,
        "last_emoji": ServerState.last_emoji,
        "local_ip": ServerState.local_ip,
        "port": PORT,
        "buffer": emoji_buffer.get_display_text(),
        }
    )

    socketio.emit(
        UPDATE_ADMIN, 
        { 
            "keyboard_running": ServerState.keyboard_running,
            "display_clients": ServerState.display_clients, 
            "control_clients": ServerState.control_clients, 
            "last_key": ServerState.last_key, 
            "last_emoji": ServerState.last_emoji, 
            "local_ip": ServerState.local_ip, 
            "port": PORT, 
            "buffer": emoji_buffer.get_display_text(),  
        }, 
    )