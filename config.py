from pathlib import Path 
import json 

BASE_DIR = Path(__file__).resolve().parent 

with open(BASE_DIR / "config.json", encoding="utf-8") as file: 
    CONFIG = json.load(file) 

HOST = CONFIG["server"]["host"] 

PORT = CONFIG["server"]["port"] 

KEY_MAP = CONFIG["keyboard"]["key_map"] 