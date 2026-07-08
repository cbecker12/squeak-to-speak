import threading 
import keyboard 
import services.emoji_service as emoji_service 
from config import KEY_MAP 

def on_key(event): 
    
    key = event.name.lower() 

    if key not in KEY_MAP: 
        return 
    
    emoji = KEY_MAP[key] 
    print(f"{key} -> {emoji}") 
    emoji_service.add_emoji(emoji) 

def start(): 

    keyboard.on_press(on_key) 
    print("Keyboard listener started.") 
    keyboard.wait()  
