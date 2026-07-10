import threading 
import keyboard 
import services.emoji_service as emoji_service 
from config import KEY_MAP 
from shared.state import ServerState 

def on_key(event): 
    
    key = event.name.lower() 

    if key not in KEY_MAP: 
        return 
    
    ServerState.last_key = key 
    
    emoji = KEY_MAP[key] 
    ServerState.last_emoji = emoji 
    print(f"{key} -> {emoji}") 
    emoji_service.add_emoji(emoji) 

def start(): 
    try: 
        ServerState.keyboard_running = True 
        keyboard.on_press(on_key) 
        print("Keyboard listener started.") 
        keyboard.wait()  
    finally: 
        ServerState.keyboard_running = False 
